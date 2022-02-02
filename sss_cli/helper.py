import enum
import json
from dataclasses import dataclass
from pathlib import Path

import typer

from sss_cli import APP_NAME, __version__

NOT_SET = str(enum.auto())


class NoKeychainException(Exception):
    pass


def get_keychain() -> Path:
    app_dir = Path(typer.get_app_dir(APP_NAME))
    app_dir.mkdir(parents=True, exist_ok=True)
    keychain: Path = app_dir / "keychain.json"
    return keychain


def write_file(file_path: Path, file_content: str) -> None:

    with open(file_path, "wb") as env_file:
        env_file.write(file_content.encode("utf-8"))
    typer.secho(f"Successfully write file to {file_path}", fg="green")


@dataclass(frozen=True)
class File_Map:
    source: str
    target: Path


class Config_Manager:
    def __init__(self) -> None:
        self.config_id: str = NOT_SET
        self.files: list[File_Map] = [File_Map(source=NOT_SET, target=Path())]
        self.key_identifier: str = NOT_SET
        self.last_key_rotation: int = 0
        self.sss_version: str = NOT_SET

    def load(self, config_path: Path) -> None:
        if not config_path.exists():
            typer.secho(f"Config file not found: {config_path}", fg="red")
            raise typer.Exit(code=1)
        folder = Path(config_path).parent
        with open(config_path, "r") as config_file:
            config_dict = json.loads(config_file.read())

        self.sss_version = config_dict["sss_version"]
        self.check_version()

        file_maps = []
        for file in config_dict["files"]:
            abs_target: Path = folder / file["target"]
            file_maps += [File_Map(file["source"], abs_target.absolute())]
        self.config_id = config_dict["config_id"]
        self.files = file_maps
        self.key_identifier = config_dict["key_identifier"]
        self.last_key_rotation = config_dict["last_key_rotation"]

    def check_version(self):
        if not self.sss_version == __version__:
            typer.secho(
                f"sss_cli version {__version__} and config version {self.sss_version} mismatch",
                fg="red",
            )
            raise typer.Exit(code=1)


config = Config_Manager()

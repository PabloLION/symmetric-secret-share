import enum
import json
from pathlib import Path

import typer

from sss_cli import APP_NAME

USE_KEYCHAIN = str(enum.auto())
NOT_SET = str(enum.auto())


class NoKeychainException(Exception):
    pass


def get_keychain() -> Path:
    app_dir = Path(typer.get_app_dir(APP_NAME))
    app_dir.mkdir(parents=True, exist_ok=True)
    keychain: Path = app_dir / "keychain.json"
    return keychain


def throw_error(err_msg: str) -> None:
    typer.secho(err_msg, fg="red")
    typer.Abort()
    raise Exception(err_msg)


def write_file(file_path: str, file_content: str) -> None:

    with open(file_path, "wb") as env_file:
        env_file.write(file_content.encode("utf-8"))
    typer.secho(f"Successfully write file to {file_path}", fg="green")


def check_exist(file_path: Path) -> None:
    if not file_path.exists():
        throw_error(
            f"path `{file_path}` does not exist, must use an existing repo_path"
        )


def load_config(folder_path: Path) -> None:
    check_exist(folder_path)
    with open(folder_path / ".sss.json", "r") as config_file:
        config_string = config_file.read()
    config_dict = json.loads(config_string)
    config.source = config_dict.get("source_url")
    config.target = config_dict.get("target_rel_path")
    config.config_id = config_dict.get("config_id")


class Config_Manager:
    def __init__(self):
        self._source = NOT_SET
        self._target = NOT_SET
        self._config_id = NOT_SET

    @property
    def source(self):
        """Get source path."""
        return self._source

    @source.setter
    def source(self, source: str):
        """Set source path."""
        self._source = source

    @property
    def target(self):
        """Get target path."""
        return self._target

    @target.setter
    def target(self, target: str):
        """Set target path."""
        self._target = target

    @property
    def config_id(self):
        """Get config id."""
        return self._config_id

    @config_id.setter
    def config_id(self, config_id: str):
        """Set config id."""
        self._config_id = config_id


config = Config_Manager()

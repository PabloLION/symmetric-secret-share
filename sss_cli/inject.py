import json
import os
from pathlib import Path

import typer

from ._helper import config, throw_error, write_file, load_config
from .encryption import decrypt
from .remote import fetch_encrypted


def inject(
    target_path: str = typer.Argument(..., help="path to your repo"),
    key: str = typer.Option(..., "-k", "--key", help="password as plaintext"),
):
    """Inject the decrypted cypher to correct path in repo."""

    typer.secho("TODO: Currently no decrypt. Key not used", fg="yellow")
    config_path = Path(target_path) / ".sss.json"
    load_config(config_path)
    plain_secret = decrypt_cypher(config.source, key)
    inject_files(
        folder_path=target_path,
        file_rel_path=config.target,
        file_content=plain_secret,
    )
    return 0


def decrypt_cypher(source_url: str, key: str) -> str:

    typer.echo(f"decrypting cypher with {key}.")
    cypher_string = fetch_encrypted(source_url)
    # TODO: decrypt cypher_string
    plain_secret = decrypt(cypher_string, key)
    return plain_secret


def inject_files(folder_path: str, file_rel_path: str, file_content: str) -> None:
    def gen_dotenv_path(repo_path: str) -> str:
        if not os.path.exists(repo_path):
            throw_error("repo_path does not exist, must use an existing repo_path")
        if not os.path.isdir(repo_path):
            throw_error("repo_path is not a directory, must use a valid repo_path")
        return os.path.join(repo_path, file_rel_path)

    write_file(gen_dotenv_path(folder_path), file_content)

from pathlib import Path

import typer

from sss_cli.keychain import get_real_key

from .encryption import encrypt
from .helper import config, write_file


def share(
    config_path: str = typer.Argument(..., help="Path to your repo"),
    key: str = typer.Option("", "-k", "--key", help="Password as plaintext"),
):
    """Update the cypher file by encrypting the secret file."""
    config.load(Path(config_path))
    key = get_real_key(key)
    for file in config.files:
        with open(file.target, "rb") as secret_file:
            secret_string = secret_file.read().decode("utf-8")
        write_file(file.target.with_suffix(".encrypted"), encrypt(secret_string, key))
        typer.secho("TODO: Manually upload and delete the encrypted file", fg="yellow")
        typer.secho("Encrypted file not uploaded/deleted", fg="red")

from pathlib import Path
import typer

from sss_cli.keychain import get_real_key

from .helper import (
    USE_KEYCHAIN,
    config,
    write_file,
    load_config,
)
from .encryption import encrypt


def share(
    target_path: str = typer.Argument(..., help="Path to your repo"),
    key: str = typer.Option(USE_KEYCHAIN, "-k", "--key", help="Password as plaintext"),
):
    """Update the cypher file by encrypting the secret file."""
    # load global config
    target = Path(target_path)
    load_config(target)
    secret = target / config.target
    # CLI options
    key = get_real_key(key)
    # encrypt
    with open(secret, "rb") as secret_file:
        secret_string = secret_file.read().decode("utf-8")
    write_file(str(secret.with_suffix(".encrypted")), encrypt(secret_string, key))
    typer.secho("TODO: Manually upload and delete the encrypted file", fg="yellow")
    typer.secho("Encrypted file not uploaded/deleted", fg="red")

from pathlib import Path
import typer

from .helper import config, throw_error, write_file, load_config
from .encryption import encrypt


def share(
    target_path: str = typer.Argument(..., help="Path to your repo"),
    key: str = typer.Option(..., "-k", "--key", help="Password as plaintext"),
):
    """Update the cypher file by encrypting the secret file."""
    typer.secho("TODO: Currently no encrypt. Key not used", fg="yellow")
    target = Path(target_path)
    load_config(target)
    secret = target / config.target

    with open(secret, "rb") as secret_file:
        secret_string = secret_file.read().decode("utf-8")
    write_file(str(secret.with_suffix(".encrypted")), encrypt(secret_string, key))
    typer.secho("TODO: Manually upload and delete the encrypted file", fg="yellow")
    typer.secho("Encrypted file not uploaded/deleted", fg="red")

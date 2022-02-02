from pathlib import Path

import typer

from sss_cli.keychain import get_real_key

from .encryption import decrypt
from .helper import config, write_file
from .remote import fetch_encrypted


def inject(
    config_path: str = typer.Argument(..., help="Path to your config_file"),
    key: str = typer.Option("", "-k", "--key", help="Password as plaintext"),
):
    """Inject the decrypted cypher to correct path in repo."""

    config.load(Path(config_path))
    # CLI options
    key = get_real_key(key)
    for file in config.files:
        cypher_string = fetch_encrypted(file.source)
        plain_secret = decrypt(cypher_string, key)
        write_file(file.target, plain_secret)

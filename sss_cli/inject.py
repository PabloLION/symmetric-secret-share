import os
from pathlib import Path

import typer

from sss_cli.keychain import get_real_key

from .encryption import decrypt
from .helper import USE_KEYCHAIN, config, load_config, throw_error, write_file
from .remote import fetch_encrypted


def inject(
    target_path: str = typer.Argument(..., help="Path to your repo"),
    key: str = typer.Option(USE_KEYCHAIN, "-k", "--key", help="Password as plaintext"),
):
    """Inject the decrypted cypher to correct path in repo."""

    load_config(Path(target_path))
    # CLI options
    key = get_real_key(key)
    cypher_string = fetch_encrypted(config.source)
    plain_secret = decrypt(cypher_string, key)

    inject_files(
        folder_path=target_path,
        file_rel_path=config.target,
        file_content=plain_secret,
    )
    return 0


def inject_files(folder_path: str, file_rel_path: str, file_content: str) -> None:
    def gen_dotenv_path(repo_path: str) -> str:
        if not os.path.exists(repo_path):
            throw_error("repo_path does not exist, must use an existing repo_path")
        if not os.path.isdir(repo_path):
            throw_error("repo_path is not a directory, must use a valid repo_path")
        return os.path.join(repo_path, file_rel_path)

    write_file(gen_dotenv_path(folder_path), file_content)

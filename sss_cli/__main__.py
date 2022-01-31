from io import open_code
from os import error, path
import os.path
import typer

from sss_cli import APP_NAME
from sss_cli.inject import inject
from sss_cli.helper import write_file
from sss_cli.encryption import encrypt
from sss_cli.share import share


app = typer.Typer()


@app.command(name="inject")
def cmd_inject(
    repo_path: str = typer.Argument(..., help="path to your repo"),
    key: str = typer.Option(..., "-k", "--key", help="password as plaintext"),
):
    """Inject the decrypted cypher to correct path in repo."""
    inject(repo_path, key)


def get_paths() -> dict[str, str]:
    file_dir = os.path.dirname(os.path.abspath(__file__))
    root = os.path.join(file_dir, "..")
    return {
        "ROOT": root,
        "SECRET_FILE": os.path.join(root, "secret", "secret.env"),
        "CYPHER_FILE": os.path.join(root, "cypher", "encrypted"),
    }


PATHS: dict[str, str] = get_paths()


@app.command("helper")
def helper():
    app_dir = typer.get_app_dir(APP_NAME)
    print(f"app_dir: {app_dir}")


@app.command("key")
def set_key():
    app_dir = typer.get_app_dir(APP_NAME)
    print(f"app_dir: {app_dir}")


@app.command("share")
def cmd_share(
    target_path: str = typer.Argument(..., help="path to your repo"),
    key: str = typer.Option(..., "-k", "--key", help="password as plaintext"),
):
    """Update the cypher file by encrypting the secret file."""
    share(target_path, key)

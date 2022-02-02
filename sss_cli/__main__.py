from pathlib import Path
from xmlrpc.client import boolean
import typer

from sss_cli import APP_NAME, __version__
from sss_cli.inject import inject
from sss_cli.share import share
from sss_cli._string_template import EXAMPLE_KEYCHAIN

app = typer.Typer()


@app.command(name="inject")
def cmd_inject(
    repo_path: str = typer.Argument(..., help="path to your repo"),
    key: str = typer.Option(..., "-k", "--key", help="password as plaintext"),
):
    """Inject the decrypted cypher to correct path in repo."""
    inject(repo_path, key)


@app.command("helper")
def helper():
    app_dir = typer.get_app_dir(APP_NAME)
    print(f"app_dir: {app_dir}")


@app.command("key")
def set_key(
    clear: boolean = typer.Option(
        False, "-c", "--clear", help="clear all keys in keychain"
    ),
):
    app_dir = typer.get_app_dir(APP_NAME)
    app_dir_path = Path(app_dir)
    app_dir_path.mkdir(parents=True, exist_ok=True)
    keychain_path: Path = Path(app_dir) / "keychain.json"
    if not keychain_path.is_file():
        keychain_path.write_text(EXAMPLE_KEYCHAIN)
    typer.echo("Opening keychain config file.")
    typer.launch(str(keychain_path))


@app.command("share")
def cmd_share(
    target_path: str = typer.Argument(..., help="path to your repo"),
    key: str = typer.Option(..., "-k", "--key", help="password as plaintext"),
):
    """Update the cypher file by encrypting the secret file."""
    share(target_path, key)

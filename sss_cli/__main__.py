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
    repo_path: str = typer.Argument(..., help="Path to your repo"),
    key: str = typer.Option(..., "-k", "--key", help="Password as plaintext"),
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
        False, "-c", "--clear", help="Clear all keys in keychain"
    ),
    force: boolean = typer.Option(
        False, "-f", "--force", help="Force clear all keys in keychain"
    ),
):
    """Edit keys in keychain."""
    app_dir = Path(typer.get_app_dir(APP_NAME))
    app_dir.mkdir(parents=True, exist_ok=True)
    keychain: Path = app_dir / "keychain.json"
    if clear:
        if not force:
            typer.confirm("Are you sure you want to delete it?", abort=True)
        if keychain.is_file():
            keychain.unlink()
            typer.secho("Cleared keychain.", fg="green")
        return
    if not keychain.is_file():
        keychain.write_text(EXAMPLE_KEYCHAIN)
    typer.secho("Please edit keychain config file.", fg="green")
    typer.launch(str(keychain))


@app.command("share")
def cmd_share(
    target_path: str = typer.Argument(..., help="Path to your repo"),
    key: str = typer.Option(..., "-k", "--key", help="Password as plaintext"),
):
    """Update the cypher file by encrypting the secret file."""
    share(target_path, key)

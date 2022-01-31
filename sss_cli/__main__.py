from io import open_code
from os import error, path
import os.path
import typer

from sss_cli import APP_NAME
from .encryption import decrypt, encrypt


app = typer.Typer()


def get_static_paths() -> dict[str, str]:
    file_dir = os.path.dirname(os.path.abspath(__file__))
    root = os.path.join(file_dir, "..")
    return {
        "ROOT": root,
        "SECRET_FILE": os.path.join(root, "secret", "secret.env"),
        "CYPHER_FILE": os.path.join(root, "cypher", "encrypted"),
    }


global PATHS
PATHS: dict[str, str] = get_static_paths()


def throw_error(err_msg: str) -> None:
    typer.secho(err_msg, fg="red")
    typer.Abort()
    raise error(err_msg)


def write_file(file_path: str, file_content: str) -> None:

    with open(file_path, "wb") as env_file:
        env_file.write(file_content.encode("utf-8"))
    typer.secho(f"Successfully write file to {file_path}", fg="green")


@app.command("helper")
def helper():
    app_dir = typer.get_app_dir(APP_NAME)
    print(f"app_dir: {app_dir}")


@app.command("key")
def set_key():
    app_dir = typer.get_app_dir(APP_NAME)
    print(f"app_dir: {app_dir}")


@app.command("enc")
def cmd_encrypt(
    key: str = typer.Option(..., "-k", "--key", help="password as plaintext"),
    secret_path: str = typer.Option(
        PATHS["SECRET_FILE"], "-s", "--secret", help="path to secret file"
    ),
):
    """Update the cypher file by encrypting the secret file."""
    typer.secho("TODO: Currently no encrypt. Key not used", fg="yellow")
    with open(secret_path, "rb") as secret_file:
        secret_string = secret_file.read().decode("utf-8")
    write_file(PATHS["CYPHER_FILE"], encrypt(secret_string, key))


@app.command("dec")
def cmd_decrypt(
    repo_path: str = typer.Argument(..., help="path to your repo"),
    key: str = typer.Option(..., "-k", "--key", help="password as plaintext"),
    edit: bool = typer.Option(
        False, "-e", "--edit", help="generate file in secret to edit"
    ),
):
    """Inject the decrypted cypher to correct path in repo."""

    typer.secho("TODO: Currently no decrypt. Key not used", fg="yellow")
    plain_secret = decrypt_cypher_file(key)
    inject_dotenv(repo_path, plain_secret)
    if edit:
        write_file(PATHS["SECRET_FILE"], plain_secret)
    return 0


def decrypt_cypher_file(key: str) -> str:

    typer.echo(f"decrypting cypher with {key}.")
    with open(PATHS["CYPHER_FILE"], "rb") as cypher_file:
        cypher_string = cypher_file.read().decode("utf-8")
    # TODO: decrypt cypher_string
    plain_secret = decrypt(cypher_string, key)
    return plain_secret


def inject_dotenv(repo_path: str, env_string: str) -> None:
    def gen_dotenv_path(repo_path: str) -> str:
        if not os.path.exists(repo_path):
            throw_error("repo_path does not exist, must use an existing repo_path")
        if not os.path.isdir(repo_path):
            throw_error("repo_path is not a directory, must use a valid repo_path")
        # different repos may have different place to store secrets
        # for repo_name in REPO_SETTINGS:
        #     if repo_name == os.path.basename(os.path.abspath(repo_path)):
        #         return os.path.join(repo_path, REPO_SETTINGS[repo_name]["env_path"])
        # throw_error("repo_path does not match any repo in REPO_SETTINGS")
        return "error"  # for type checking

    write_file(gen_dotenv_path(repo_path), env_string)


if __name__ == "__main__":
    app()

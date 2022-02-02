import json

import typer

from sss_cli import __version__
from sss_cli.helper import NoKeychainException, config, get_keychain


def load_key_from_chain(config_id: str) -> str:
    keychain = get_keychain()
    if not keychain.is_file():
        typer.secho("Keychain file not found, please run `sss key` first", fg="red")
        raise NoKeychainException
    with open(keychain, "r") as keychain_file:
        keychain_dict = json.load(keychain_file)
        if not keychain_dict["version"] == __version__:
            typer.secho(
                f"Keychain file version {keychain_dict['version']} and current version {__version__} do not match",
                fg="red",
            )
    try:
        key = keychain_dict.get("keys").get(config_id).get("key")
    except (AttributeError, KeyError):
        typer.secho(f"Keychain file does not contain `keys` or `{config_id}`", fg="red")
        raise NoKeychainException
    if not key:
        typer.secho(
            f"Keychain file does not contain key for config_id `{config_id}`", fg="red"
        )
        raise NoKeychainException
    return key


def get_real_key(key: str) -> str:
    if key == "":
        try:
            key = load_key_from_chain(config.config_id)
        except NoKeychainException:
            typer.secho("No keychain found, please run `sss key` first", fg="red")
            raise typer.Exit(code=1)

    return key

from codecs import encode, decode
import nacl.utils
import nacl.secret
import nacl.exceptions
import typer


def encrypt(message: str, key: str) -> str:
    """
    Encrypt string with key
    """
    try:
        box = nacl.secret.SecretBox(encode(key, "utf-8"))
    except nacl.exceptions.ValueError:
        typer.secho("The key must be exactly 32-char long ", fg="red")
        raise typer.Exit(code=1)
    encrypted = box.encrypt(encode(message, "utf-8"))
    b64 = encode(encrypted, "base64").decode("utf-8")
    return b64


def decrypt(encrypted: str, key: str) -> str:
    """
    Encrypt string with key
    """
    try:
        box = nacl.secret.SecretBox(encode(key, "utf-8"))
    except nacl.exceptions.ValueError:
        typer.secho("The key must be exactly 32-char long ", fg="red")
        raise typer.Exit(code=1)
    byte_msg = decode(encode(encrypted, "utf-8"), "base64")
    try:
        decrypted = box.decrypt(byte_msg).decode("utf-8")
    except nacl.exceptions.CryptoError:
        typer.secho("Decryption failed. Ciphertext failed verification", fg="red")
        raise typer.Exit(code=1)
    return decrypted


def test():
    fake_key = "I'm a sentence of 32 characters."  # 32 one-byte characters
    fake_key = "4}M?XW]:`TqSP9/m2RW]l-Tatx0bFVa,"  # 32 one-byte characters
    fake_key = "ǕèǶ¿§ܚøө½ߊƎǏƵǪИ"  # 32 two-byte characters
    fake_key = "ݒȄԸưŘ͎ɡҜȐѽژ̎ʶܐڝؔ"
    msg = "I'm a secret message."

    encrypted = encrypt(msg, fake_key)
    decrypted = decrypt(encrypted, fake_key)

    print(f"encrypted: \n{encrypted}")
    print(f"decrypted: \n{decrypted}")


if __name__ == "__main__":
    test()

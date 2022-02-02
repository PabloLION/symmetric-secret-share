import codecs
import nacl.utils
import nacl.secret


def encrypt(message: str, key: str) -> str:
    """
    Encrypt string with key
    """
    # TODO: add a try catch here or outside for nacl.exceptions.CryptoError: Decryption failed. Ciphertext failed verification
    box = nacl.secret.SecretBox(codecs.encode(key, "utf-8"))
    encrypted = box.encrypt(codecs.encode(message, "utf-8"))
    b64 = codecs.encode(encrypted, "base64").decode("utf-8")
    return b64


def decrypt(encrypted: str, key: str) -> str:
    """
    Encrypt string with key
    """
    box = nacl.secret.SecretBox(codecs.encode(key, "utf-8"))
    byte_msg = codecs.decode(bytes(encrypted, "utf-8"), "base64")
    decrypted = box.decrypt(byte_msg).decode("utf-8")
    return decrypted


def test():
    fake_key = "I'm a sentence of 32 characters."
    msg = "i'm a secret message, but not a sentence, very very very long lorem ipsum dolor, very very very long lorem ipsum dolor, very very very long lorem ipsum dolor, very very very long lorem ipsum dolor, very very very long lorem ipsum dolor, very very very long lorem ipsum dolor, very very very long lorem ipsum dolor, very very very long lorem ipsum dolor"

    encrypted = encrypt(msg, fake_key)
    decrypted = decrypt(encrypted, fake_key)

    print(f"encrypted: \n{encrypted}")
    print(f"decrypted: \n{decrypted}")


if __name__ == "__main__":
    test()

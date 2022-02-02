from sss_cli import __version__
import json

EXAMPLE_KEYCHAIN_DICT = {
    "version": f"{__version__}",
    "keys": {
        "sss-example": {
            "key": "This key contains 32 characters.",
            "comment": "Some comment. This key is used for testing.",
        }
    },
}

EXAMPLE_KEYCHAIN = json.dumps(EXAMPLE_KEYCHAIN_DICT, indent=2)


def test_keychain_dict():
    print(EXAMPLE_KEYCHAIN_DICT)


if __name__ == "__main__":
    test_keychain_dict()

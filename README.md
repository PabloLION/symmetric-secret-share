# symmetric-secret-share

Python CLI to share secret files via github with symmetric encryption ed25519.

- **IMPORTANT: The secret files should be git-ignored to avoid oblivious leakage.**
- Temporarily supports only text files (only tested with `.env`).
- Best used to store/share secrets and configurations.
- Key should be a 32-byte long string, meanly, 32 ASCII, 16 two-byte UTF-8 or 8 four-byte UTF-8 characters.
- (FAQ) If you share with GitHub (like the example), please notice that there's a 5 minutes cool-down on refreshing. [Detail](https://stackoverflow.com/questions/46551413/github-not-update-raw-after-commit) However, GitHub Gist seems doesn't have this cool-down limitation.

## Use

1. Install CLI: `pip3 install symmetric-secret-share`.
2. Check the [Tutorial Chapter](#Tutorial) and `sss --help`.
3. Recommended: set up a global key chain with `sss key`, or you would have to input a key every time.
4. Get a config like `$REPO_ROOT/tests/injection/sss.json`. The JSON-schema in `$schema` of this file will help you write the config file.

### inject

1. Get a config file like `$REPO_ROOT/tests/injection/sss.json`.
2. Run CLI

   ```bash
   sss inject [-k TEXT] CONFIG_PATH
   ```

### share

1. Run CLI

   ```bash
   sss share [-k TEXT] CONFIG_PATH
   ```

### key

1. Run CLI

   ```bash
   sss key [-c/f/g] # -g: generate one key, -c: clear key chain, -f: force
   ```

2. Upload the generated file to GitHub (or other platforms).
3. Update the config file if needed.

## Security

- There are `256**32==1,15e+77` keys of 32 of ASCII (one-byte utf-8 string).
- To generate ASCII key, you can use `sss key --generate`.
- To generate two-byte utf-8 string, a possibility is to use [onlineutf8tools](https://onlineutf8tools.com/generate-random-utf8?&length=16&count=8&bytes-per-char=2)

## Contribute

- Created for [Artcoin-Network](https://github.com/Artcoin-Network/), modifying a private repo [Artcoin-Network/artificial-dev-config](https://github.com/Artcoin-Network/artificial-dev-config).
- To contribute, please fork the repo and run `poetry install`.
- Read more in [CONTRIBUTE.md](./docs/CONTRIBUTE.md)

## Tutorial

In this tutorial, all commands are assumed to be run under the `$REPO_ROOT`. We are going to use these concepts and variables:

- key chain: A file to share key, initialized with `sss key`.
- key: `This key contains 32 characters.`.
- URL: `https://raw.githubusercontent.com/PabloLION/symmetric-secret-share/main/tests/example.encrypted`.

We are going to play with the folder `test/injection`, with the `sss.json` file inside it. To share your own file, a new config file should be created.

### Setup a local key chain

```bash
sss key # create/edit
sss key -c # clear all keys
```

### load files from URL

These code will generate a `test/injection/target.env` like `test/example.env`

```bash
sss inject ./tests/injection/sss.json # use key from initial key chain
sss inject -k "This key contains 32 characters." ./tests/injection/sss.json
sss inject ./tests/injection/sss.json -k "I'm a string with 32 characters." # fail
```

### share files

Need to upload manually #TODO
These code will generate a `test/injection/target.encrypted`

```bash
sss share ./tests/injection/sss.json # use key from initial key chain
sss share -k "This key contains 32 characters." ./tests/injection/sss.json
```

# symmetric-secrete-share

Share secret files via github with symmetric encryption

- Temporarily supports only `.env` files.
- Used to store secrets and configurations.
- **IMPORTANT: The secret files at should be git-ignored.**
- Key should be a 32-byte long string.
- (FAQ) If you share with GitHub, please notice that there's a 5 minutes cool-down on refreshing. [Details](https://stackoverflow.com/questions/46551413/github-not-update-raw-after-commit)

## Use

1. Install CLI
2. Have a global config for the secret keys.
3. Setup a config file in the target folder.
4. Check the [Tutorial](#Tutorial) and `sss --help`

### fetch

1. Make sure the config file exists.
2. Run CLI

### share

- **IMPORTANT: The generated secret (`*.encrypted`) at should be git-ignored to avoid oblivious leakage.**

1. Upload an encrypted file to GitHub (or other platforms).

## Contribute

- Created for [Artcoin-Network](https://github.com/Artcoin-Network/), modifying the private repo[Artcoin-Network/artificial-dev-config](https://github.com/Artcoin-Network/artificial-dev-config).
- Read More in [dev-docs.md](./docs/dev-docs.md)

## Tutorial

In this tutorial, we are going to use these concepts:

- key: `This key contains 32 characters.`
- URL: `https://raw.githubusercontent.com/PabloLION/symmetric-secrete-share/main/tests/example.encrypted`
- key chain: Need to initialize with `sss key`

### Setup a local key chain

```bash
sss key # create/edit
sss key -c # clear all keys
```

### load file from URL

```bash
sss inject -k "This key contains 32 characters." ./tests/injection-target
sss inject ./tests/injection-target -k "I'm a string with 32 characters." # fail
sss inject ./tests/injection-target # use key from initial key chain
```

### share file to the URL

Need to upload manually #TODO

```bash
sss share -k "This key contains 32 characters." ./tests/injection-target
sss share ./tests/injection-target # use key from initial key chain
```

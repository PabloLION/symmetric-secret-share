# Development Documentation

## Version

### 0.0.5

- Publish to PyPI

### 0.0.4

- Add `poetry`
- Add and chang json schema many times.
- Finish DEV LOG 7~15.

### 0.0.2

- Work in [Artcoin-Network/artificial-dev-config](https://github.com/Artcoin-Network/artificial-dev-config).
- Finish DEV LOG 1~6.

## DEV LOG

1. (DONE) Add a script to generate different files from one same file. We always use `.env`
2. (DONE) Use the CLI in (1) to write to the right place.
3. (DONE) Add a script to decrypt and encrypt.
   1. check [grempe/secrets.js](https://github.com/grempe/secrets.js)
4. (DONE)Add a way to edit the encrypted file
5. (DONE)Add more content like `asset_name`, `decimal_digits`.
6. (NONE)This is opening a folder, not selecting one: Use GUI to select folder, see [typer official](https://typer.tiangolo.com/tutorial/launch/#locating-a-file).
7. (DONE)Add key to ~~system variable~~ a local key chain and use it, instead of writing it every time.
8. (DONE)Use a descriptive config file in each repo to specify the path of the encrypted file, also supporting CLI execution from the external repo folder.
9. (DONE)Fetch file from cloud instead from this repo locally. (from local will require git pull every time before running it)
10. (NONE)GUI: tkinter to select config file
11. (MOVE)Last key rotation
12. (DONE)Select a config file, not folder.
13. (DONE)throw_error,check_exist
14. (DONE)settings version confirm
15. (DONE)use absolute path (no $SOME_PATH/./../file)

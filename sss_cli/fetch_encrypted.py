import requests
import typer

url = "https://raw.githubusercontent.com/PabloLION/usehooks-ts/master/tsconfig.json"


def fetch_encrypted(url):
    try:
        r = requests.get(url)
        return r
    except:
        typer.secho(f"Error fetching {url}", fg="red")
        typer.Abort()
        raise Exception(f"Error fetching {url}")

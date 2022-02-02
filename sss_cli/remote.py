import requests
import typer


def fetch_encrypted(url):
    try:
        r = requests.get(url).text
        return r
    except:
        typer.secho(f"Error fetching {url}", fg="red")
        raise typer.Exit(code=1)

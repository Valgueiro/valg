import typer

app = typer.Typer()

@app.command()
def hello(name: str):
    typer.echo(f"Hello {name}")

@app.callback()
def callback():
    """
    Valg utils
    """


# Start
1. install poetry and python
2. $ poetry new <project>
3. $ poetry add typer
4. Setup vscode python env
5. Add typer hello world
6. $ poetry run python valg/main.py bla

...https://typer.tiangolo.com/tutorial/package/


```
import typer

app = typer.Typer()

@app.callback()
def callback():
    """
    My project utils
    """


@app.command()
def hello(name: str):
    typer.echo(f"Hello {name}")
```

$ valg

$ valg hello world

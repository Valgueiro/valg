import typer

from psutil import process_iter, AccessDenied
from signal import SIGTERM # or SIGKILL


app = typer.Typer()

@app.command()
def hello(name: str):
    typer.echo(f"Hello {name}")

@app.callback()
def callback():
    """
    Valg utils
    """
    
@app.command()
def freeport(port: int):
    """
    Free port from running processes
    """
    for proc in process_iter():
        try:  
            for conns in proc.connections(kind='inet'):
                if conns.laddr.port == port:
                    proc.send_signal(SIGTERM)
                    typer.echo('Process {}: {} - stopped'.format(proc.name(), proc.pid))
        except (PermissionError, AccessDenied): 
            pass
        
    typer.echo('✅ Port {} is free now'.format(port))
    

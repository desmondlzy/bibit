import bibit.eg as eg
import typer

app = typer.Typer()

@app.command()
def bibit(filename: str):
	eg.process(filename)

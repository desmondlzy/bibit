# bibit

A simple command line tool for formatting [BibTex](http://www.bibtex.org/Format/) files :rocket::fire::books:.

## Install

Requires [poetry](https://python-poetry.org/), and python 3.8+

```
git clone https://github.com/desmondlzy/bibit && cd bibit
poetry install
```

## Usage

After installation,

```
bibit refs.bib
```

You get a output formatted file named `refs-out.bib` :boom:.

The command line interface is powered by [Typer](https://typer.tiangolo.com/).
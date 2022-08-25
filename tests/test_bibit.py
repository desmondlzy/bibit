import bibit


def test_version():
    assert bibit.__version__ == '0.1.0'


def test_cli():
    bibit.cli.bibit("test.bib")
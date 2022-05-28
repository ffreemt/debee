"""Test debee --version."""
from typer.testing import CliRunner

# from .main import app
from debee import __version__
from debee.__main__ import app

runner = CliRunner()


def test_cli_version():
    """Test debee --version."""
    # result = runner.invoke(app, ["Camila", "--city", "Berlin"])
    result = runner.invoke(app, ["--version"])

    assert result.exit_code == 0
    assert "debee" in result.stdout
    assert __version__ in result.stdout

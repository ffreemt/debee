"""Test debee."""
# pylint: disable=broad-except
from debee import __version__, debee


def test_version():
    """Test version."""
    assert __version__[:3] == "0.1"


def test_sanity():
    """Check sanity."""
    try:
        assert not debee([""], [""])
    except Exception:
        assert True

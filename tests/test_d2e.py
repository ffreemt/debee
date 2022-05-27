"""Test d2e."""
import pytest

from de2en.d2e import d2e


def test_d2e():
    """Test d2e."""

    # ['test', 'Testing', 'Test', 'testing', 'tests']
    assert "test" in d2e("Test")

    assert "Love" in d2e("Liebe")


@pytest.mark.xfail(raises=KeyError)
def test_d2e_keyerror():
    """Test d2e fail."""
    assert d2e("test")  # KeyError

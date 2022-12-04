"""
Test program call from command line.
"""

import pytest

import squarer


def test_entrypoint(capsys: pytest.CaptureFixture) -> None:
    # pylint: disable=too-many-function-args
    squarer.console_entry_point(["1.0"])

    out, err = capsys.readouterr()
    assert out == "1.0\n"
    assert err == ""

"""
Test program call from command line.
"""

import pytest

import squarer


def test_main(capsys: pytest.CaptureFixture) -> None:
    squarer.main(["1.0"])  # pylint: disable=too-many-function-args

    out, err = capsys.readouterr()
    assert out == "1.0\n"
    assert err == ""

"""
Test the squaring function.
"""

from __future__ import annotations

import numpy as np
import pytest

from squarer.maths import square_a_number


@pytest.mark.parametrize("value", [1.0, 2, 3.0])
def test_squarer(value: int | float) -> None:
    assert pytest.approx(square_a_number(value)) == value * value


def test_squarer_fail() -> None:
    with pytest.raises(TypeError):
        square_a_number("2")  # type: ignore


def test_dummy() -> None:
    arr = np.array([1.0]) / 3.0
    print(arr)


def test_error() -> None:
    with pytest.raises(ZeroDivisionError):
        _ = 1 / 0

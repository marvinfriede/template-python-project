"""
Test the squaring function.
"""

from __future__ import annotations

import pytest

from squarer.maths import square_a_number


@pytest.mark.parametrize("value", [1.0, 2, 3.0])
def test_add(value: int | float) -> None:
    assert pytest.approx(square_a_number(value)) == value * value

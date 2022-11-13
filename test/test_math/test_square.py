import pytest
from squarer.maths import square_a_number


def test_add() -> None:
  assert pytest.approx(square_a_number(2.0)) == 4.0
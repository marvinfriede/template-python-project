import pytest
from project.add import add_floats


def test_add() -> None:
  assert pytest.approx(add_floats(1.0, 2.0)) == 3.0
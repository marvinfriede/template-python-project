def add_floats(a: float, b: float) -> float:
  if not all(isinstance(i, int) for i in [a, b]):
    raise TypeError("Only floats can be passed.")

  return a + b


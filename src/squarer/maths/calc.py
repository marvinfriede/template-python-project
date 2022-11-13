def square_a_number(a: float) -> float:
    if not isinstance(a, (float)):
        raise TypeError("Float or int expected.")

    return a * a

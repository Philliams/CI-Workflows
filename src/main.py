def dummy_function(a:int, b:int) -> int:
    """
    This is a dummy function to demonstrate docstrings being used to generate
    automatic documentation.

    :param a: A dummy integer value
    :type a: int

    :param b: A dummy integer value
    :type b: int


    :return: A dummy return value
    :rtype: int
    """
    return (a * a) - (2 * a * b) + (b * b)


if __name__ == "__main__":  # pragma: no cover
    print("Hello World!")
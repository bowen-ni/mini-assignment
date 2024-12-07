
def power(base, exponent):
    """Raises a number to a given power."""
    return base ** exponent

def divide(numerator, denominator):
    """Divides two numbers, raising an error if the denominator is zero."""
    if denominator == 0:
        raise ValueError("Cannot divide by zero.")
    return numerator / denominator


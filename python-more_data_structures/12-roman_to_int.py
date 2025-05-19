#!/usr/bin/python3
def roman_to_int(numeral):
    """
    Convert a Roman numeral to an integer between 1 and 3999.

    Args:
        numeral (str): Roman numeral to convert.

    Returns:
        int: Converted integer, or 0 for invalid input.
    """
    if not isinstance(numeral, str) or numeral is None:
        return 0

    mapping = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0
    previous = 0

    for symbol in reversed(numeral):
        current = mapping.get(symbol, 0)
        if current < previous:
            result -= current
        else:
            result += current
        previous = current

    return result

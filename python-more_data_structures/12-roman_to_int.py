#!/usr/bin/python3

def roman_to_int(roman_string):
    """
    Convert a Roman numeral to an integer
    Args:
        roman_string: string to convert
    Returns:
        Integer value of the Roman numeral, 0 if invalid input
    """
    # Dictionary mapping Roman numerals to their integer values
    numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0

    # Return 0 if input is not a valid string
    if type(roman_string) != str or roman_string is None:
        return result
    
    # Track previous value for subtractive combinations (like IV, IX, etc)
    previous = None
    for letter in roman_string:
        n = numbers[letter]

        # Handle first character case
        if previous is None:
            result = n
            previous = n
            continue
        # If current value is greater than previous, subtract twice the previous
        # (once to remove the previous addition, once for the subtraction)
        elif previous < n:
            result = result + n - previous * 2
        # Normal case: just add the current value
        else:
            result += n

        previous = n

    return result
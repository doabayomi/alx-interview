#!/usr/bin/python3
"""UTF 8 Validation
"""


def validUTF8(data):
    """Checks if list of integers are valid UTF-8

    Args:
        data: list of integers

    Returns:
        True if valid, False otherwise
    """
    remaining_bytes = 0

    for character in data:
        binary_value = f"{character:08b}"

        if remaining_bytes == 0:
            if binary_value.startswith('0'):
                continue
            elif binary_value.startswith('110'):
                remaining_bytes = 1
            elif binary_value.startswith('1110'):
                remaining_bytes = 2
            elif binary_value.startswith('11110'):
                remaining_bytes = 3
            else:
                return False
        else:
            if not binary_value.startswith('10'):
                return False
            remaining_bytes -= 1

    return remaining_bytes == 0

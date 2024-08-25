#!/usr/bin/python3
"""UTF-8 validation module.
"""


def validUTF8(data):
    """ Number of bytes in character """
    num_bytes = 0

    # Masks to identify the leading byte pattern
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    # Loop through each integer in the data list
    for num in data:
        # Mask to check the most significant bits
        mask = 1 << 7

        # If num_bytes is 0, we're looking at a new character
        if num_bytes == 0:
            # Count how many leading 1s are in the byte
            while mask & num:
                num_bytes += 1
                mask >>= 1

            # 1 byte character
            if num_bytes == 0:
                continue

            # Invalid cases
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Following bytes must start with 10xxxxxx
            if not (num & mask1 and not (num & mask2)):
                return False

        # Decrement the number of bytes left for the current character
        num_bytes -= 1

    # If we finish processing and num_bytes is not 0, it's incomplete
    return num_bytes == 0

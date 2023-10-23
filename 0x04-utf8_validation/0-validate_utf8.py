#!/usr/bin/env python3
"""a method that determines if a given data
    set represents a valid UTF-8 encoding.
"""
import chardet


def validUTF8(data):
    """a method that determines if a given data
        set represents a valid UTF-8 encoding.
    """
    trailing_bytes = 0

    for i in data:
        # get the 8 least significant bits
        i &= 0xFF

        if trailing_bytes == 0:
            # check for leading 0s
            if (i >> 7) == 0b0:   # 1 byte
                continue
            elif (i >> 5) == 0b110:  # 2 bytes sequence
                trailing_bytes = 1
            elif (i >> 4) == 0b1110:  # 3 byte sequence
                trailing_bytes = 2
            elif (i >> 3) == 0b11110:  # 4 byte sequnce
                trailing_bytes = 3
            else:
                return False
        else:
            # check if the trailing is valid
            if (i >> 6) != 0b10:
                return False
            trailing_bytes -= 1

    return trailing_bytes == 0

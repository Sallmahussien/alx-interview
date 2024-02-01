#!/usr/bin/python3
"""Defines validUTF8 function"""

from typing import List


def validUTF8(data: List[int]) -> bool:
    """Determines if a given data set represents a valid UTF-8 encoding."""
    for num in data:
        if is_valid_utf8(num) == 0:
            return False

    return True


def is_valid_utf8(c):
    if c <= 0x7F:
        return 1
    elif 0xC080 == c:
        return 1
    elif 0xC280 <= c <= 0xDFBF:
        return ((c & 0xE0C0) == 0xC080)
    elif 0xEDA080 <= c <= 0xEDBFBF:
        return 0
    elif 0xE0A080 <= c <= 0xEFBFBF:
        return ((c & 0xF0C0C0) == 0xE08080)
    elif 0xF0908080 <= c <= 0xF48FBFBF:
        return ((c & 0xF8C0C0C0) == 0xF0808080)
    else:
        return 0

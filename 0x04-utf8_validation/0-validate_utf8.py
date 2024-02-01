#!/usr/bin/python3
"""Defines validUTF8 function"""

from typing import List


def validUTF8(data: List[int]) -> bool:
    """Determines if a given data set represents a valid UTF-8 encoding."""
    for num in data:
        binary_of_num = bin(num)[2:].zfill(8)

        if (not binary_of_num.startswith('0') and
                not binary_of_num.startswith('110') and
                not binary_of_num.startswith('1110') and
                not binary_of_num.startswith('11110')):
            return False

    return True

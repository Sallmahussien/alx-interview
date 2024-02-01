#!/usr/bin/python3
"""Defines validUTF8 function"""

from typing import List


def validUTF8(data: List[int]) -> bool:
    """Determines if a given data set represents a valid UTF-8 encoding."""
    for num in data:
        if (num not in range(0, 128) and
                num not in range(49280, 57280) and
                num not in range(14712960, 15712192) and
                num not in range(4034953344, 4156538816)):
            return False

    return True

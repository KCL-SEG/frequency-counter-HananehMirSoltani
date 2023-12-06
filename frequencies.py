"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

from typing import ItemsView


def frequencies(items):
    frequency_dict = {}
    for item in items:
        # Convert the item to a string
        key = str(item)
        # Increase the count for this key in the dictionary
        if key in frequency_dict:
            frequency_dict[key] += 1
        else:
            frequency_dict[key] = 1
    return frequency_dict



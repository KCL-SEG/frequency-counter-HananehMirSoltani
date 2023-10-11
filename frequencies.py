"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

from typing import ItemsView


def frequencies(items):
    frequencies = {}
    for item in items:
        if item in frequencies:
            frequencies[item] += 1
        else:
            frequencies[item] = 1
    return frequencies
items=['a','b','c','b','a','c','a','c','b','a','c']
result = frequencies(items)

print("Frequency of items:", result)


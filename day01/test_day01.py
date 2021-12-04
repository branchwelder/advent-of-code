"""
Tests for Day 1 of Advent of Code 2021.
Author: Hannah Twigg-Smith
"""

from part1 import calculate_increases
from part2 import calculate_increases_with_frame


def test_part1():
    assert calculate_increases([3, 4, 5]) == 2
    assert calculate_increases([5, 4, 5]) == 1
    assert calculate_increases([6, 5, 4]) == 0


def test_part2():
    assert calculate_increases_with_frame([3, 4, 5]) == 0
    assert calculate_increases_with_frame([4, 5]) == 0
    assert calculate_increases_with_frame([6, 5]) == 0
    assert calculate_increases_with_frame([4, 4, 4, 5]) == 1
    assert calculate_increases_with_frame([4, 4, 4, 5, 3]) == 1
    assert calculate_increases_with_frame([4, 4, 4, 5, 6]) == 2

"""
Solution to Day 1, Part 1 of Advent of Code 2021
Author: Hannah Twigg-Smith
"""


from typing import List


def calculate_increases(nums: List[int]):
    """Takes a list of numbers and counts how many times they increase from one to the next.

    Args:
        nums (list): the list of numbers

    Returns:
        count (int): the final count of increases
    """
    last_measurement = nums[0]
    count = 0

    for meas in nums[1:]:
        current_measurement = int(meas)
        if current_measurement > last_measurement:
            count += 1
        last_measurement = current_measurement
    return count


if __name__ == "__main__":
    f = open("day01/input.txt", "r")
    nums = [int(i) for i in f.readlines()]
    print(calculate_increases(nums))

"""
Python solution to Day 1 of Advent of Code 2021
Author: Hannah Twigg-Smith
"""


from typing import List


def calculate_increases(nums: List[int]):
    """Takes a list of numbers and counts how many times they increase from one
    to the next.

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


def calculate_increases_with_frame(nums: List[int]):
    """Takes a list of numbers and counts how many times the sum of a shifting
    3-value window increases from one to the next.

    Args:
        nums (list): the list of numbers

    Returns:
        count (int): the final count of increases
    """
    count = 0
    index = 1
    prior_window_sum = sum(nums[0:3])

    while (index + 3) <= len(nums):
        window_sum = sum(nums[index : index + 3])
        if window_sum > prior_window_sum:
            count += 1
        prior_window_sum = window_sum
        index += 1

    return count


if __name__ == "__main__":
    f = open("day01/input.txt", "r")
    nums = [int(i) for i in f.readlines()]

    print("Part one solution: {}".format(calculate_increases(nums)))
    print("Part two solution: {}".format(calculate_increases_with_frame(nums)))

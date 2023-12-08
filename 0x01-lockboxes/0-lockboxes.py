#!/usr/bin/python3
"""
Module for canUnlockAll boxes
"""


def canUnlockAll(boxes):
    """
    Checks if all boxes can be opened.

    Args:
        boxes (list): A list of lists where each list represents a box
        and contains keys (positive integers).

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes or not isinstance(boxes, list):
        return False

    n = len(boxes)
    if n == 0:
        return False

    # List to keep track of opened boxes
    opened_boxes = [0]

    for box in opened_boxes:
        keys = boxes[box]

        for key in keys:
            if key < n and key not in opened_boxes:
                opened_boxes.append(key)

    # Check if all boxes have been opened
    return len(opened_boxes) == n

#!/usr/bin/python3
"""lockboses"""


def canUnlockAll(boxes):
    # method that determines if all the boxes can be opened
    if not boxes:
        return False
    # initialize variables for stack and list
    opened_boxes = set()
    opened_boxes.add(0)
    keys_stack = list(boxes[0])

    while keys_stack:
        key = keys_stack.pop()
        if key < len(boxes) and key not in opened_boxes:
            opened_boxes.add(key)
            keys_stack.extend(boxes[key])

    return len(opened_boxes) == len(boxes)

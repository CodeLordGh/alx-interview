#!/usr/bin/python3

"""
You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.
"""

def canUnlockAll(boxes):
    """
    Return true if all boxes can be opened, false if not
    """
    numberOfKeys = [0]
    numberOfBoxes = len(boxes)

    for keys in numberOfKeys:
        for box in boxes[keys]:
            if box < numberOfKey and box not in numberOfKeys:
                numberOfKeys.append(box)
    if len(numberOfKeys)  == numberOfBoxes:
        return True
    return False

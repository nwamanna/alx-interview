#!/usr/bin/python3
"""Module contains lockboxes function"""


def canUnlockAll(boxes):
    checkedBox = set()

    def dfs(idx):
        if idx not in checkedBox:
            checkedBox.add(idx)

        for key in boxes[idx]:
            if key not in checkedBox:
                checkedBox.add(key)
                dfs(key)

    dfs(0)

    return len(checkedBox) == len(boxes)

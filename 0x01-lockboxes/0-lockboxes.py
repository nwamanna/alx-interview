#!/usr/bin/python3
"""Module contains lockboxes function"""
def canUnlockAll(boxes):
    """returns true if all boxes can open"""
    # Initialize a list to store the keys found
    eleList = set()
    eleList.add(0)
    
    # Iterate through each box
    for box in boxes:
        for element in box:
            # Append each key found to eleList
            eleList.add(element)
    
    print (eleList)
    # Iterate through each box index
    for idx in range(len(boxes)):
        # Check if the index is in eleList (if we have the key)
        if idx not in eleList:
            return False  # If any box is not reachable, return False
    
    return True  
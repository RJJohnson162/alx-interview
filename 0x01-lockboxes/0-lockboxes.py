#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    :param list[list] boxes: List of lists, where each sub-list is a row in the box and contains 0s or
    Args:
        boxes (list of lists): A list of locked boxes. Each box is represented as a list of keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    visited = [False] * n
    stack = [0]  # Start with the first box, which is already unlocked

    while stack:
        current_box = stack.pop()
        visited[current_box] = True

        for key in boxes[current_box]:
            if not visited[key]:
                stack.append(key)

    return all(visited)

if __name__ == "__main__":
    # Test cases
    boxes1 = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes1))  # True

    boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes2))  # True

    boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes3))  # False

"""
Binary search algorithm.
"""

import string

alphabet = list(string.ascii_lowercase)  # is ordered list


def binary_search(item: str | int, item_list: list) -> int | None:
    """
    Perform a binary search on a sorted list.

    Args:
        item (str | int): The target value to search for.
        item_list (list): A sorted list of comparable elements (e.g., letters or numbers).

    Returns:
        int | None: The index of the target if found, otherwise None.

    Notes:
        - The input list must be sorted.
        - Works with any comparable types (e.g., str, int).
    """
    start, end = 0, len(item_list) - 1

    while start <= end:
        middle = (start + end) // 2

        if item_list[middle] == item:
            return middle

        elif item_list[middle] < item:
            start = middle + 1  # Go right

        else:
            end = middle - 1  # Gp left
    return


print(binary_search("h", alphabet))

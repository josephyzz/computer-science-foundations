"""
Binary search algorithm.
"""

import string

alphabet = list(string.ascii_lowercase)  # is ordered list


def binary_search(letter: str, alphabet_list: list) -> int | None:
    """
    Search letter and return the position or None.
    Ex: a > b = False, a < b = True
    """
    alphabet = alphabet_list
    start, end = 0, len(alphabet) - 1

    while start <= end:
        middle = (start + end) // 2

        if alphabet[middle] == letter:
            return middle

        elif alphabet[middle] < letter:
            start = middle + 1

        else:
            end = middle - 1
    return


print(binary_search("h", alphabet))

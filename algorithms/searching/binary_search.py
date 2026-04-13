"""
Binary search algorithm.
"""

import string

alphabet = list(string.ascii_lowercase)  # is ordered list


def binary_search(letter: str, alphabet_list: list) -> int | None:
    """
    Search letter and return the position or null.
    Ex: a > b = False, a < b = True
    """
    alphabet = alphabet_list
    is_continue = True
    while is_continue:
        choice = (len(alphabet) // 2) - 1
        if alphabet[choice] > letter:
            alphabet = alphabet[:choice]

        elif alphabet[choice] < letter:
            alphabet = alphabet[choice:]

        else:
            return alphabet.index(alphabet[choice])
    return


print(binary_search("d", alphabet))

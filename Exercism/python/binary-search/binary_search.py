from typing import Sequence


def find(sequence: Sequence, value) -> int:
    """This function will apply a binary search into a given sequence."""
    i = 0  # Acummulator for indexes.
    lst = sequence[::]  # Copy of original list, so I won't mess with original

    while (lenght := len(lst)) >= 1:
        m = lenght//2  # middle index of array

        if lst[m] == value:
            return m + i
        elif lenght == 1:
            break

        lst, i = (lst[m:], i + m) if lst[m] < value else (lst[:m], i)
        
    raise ValueError('value not in array')

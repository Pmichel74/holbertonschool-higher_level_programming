#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """Return a set of all elements present in only one set."""
    # Union of (set_1 - set_2) and (set_2 - set_1)
    return ((set_1 - set_2) | (set_2 - set_1))

    # ^ operator returns elements in either set but not in both
    return (set_1 ^ set_2)

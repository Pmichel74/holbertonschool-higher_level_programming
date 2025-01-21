#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """Return a set of all elements present in only one set."""

    # ^ is symmetric difference operator:
    # Returns elements that are in either set_1 or set_2, but not in both
    # Example: {1,2,3} ^ {3,4,5} = {1,2,4,5}
    return (set_1 ^ set_2)

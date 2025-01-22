#!/usr/bin/python3
def best_score(a_dictionary):
    """Return the key with the highest value in the dictionary."""
    # Check if the dictionary is empty
    # idem que if not a_dictionary
    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    # Return the key with the maximum value
    return (max(a_dictionary, key=a_dictionary.get))

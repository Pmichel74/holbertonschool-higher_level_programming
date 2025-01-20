#!/usr/bin/python3
def max_integer(my_list=[]):
    """finds the biggest integer of a list"""

    if not my_list:  # vérifie si la liste est vide
        return None

    max_num = my_list[0]  # initialise avec le premier élément
    for i in range(len(my_list)):
        if my_list[i] > max_num:
            max_num = my_list[i]

    return max_num

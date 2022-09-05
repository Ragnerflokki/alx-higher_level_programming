#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    """Find all multiples of 2 in a list."""
    multipleslist = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            multipleslist.append(True)
        else:
            multipleslist.append(False)

    return (multipleslist)

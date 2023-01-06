#!/usr/bin/env python3
""" Module for mixed lists  """


from typing import List, Union
list_fi = List[Union[int, float]]


def sum_mixed_list(mxd_lst: list_fi) -> float:
    """ takes a list mxd_lst of integers and floats,
        returns their sum as a float.
    """
    sum = 0
    for x in mxd_lst:
        sum += x
    return sum

#!/usr/bin/env python3
""" Module that returns sum of floats  """


from typing import List
list_f = List[float]


def sum_list(input_list: list_f) -> float:
    """ takes a list of floats and returns the sum"""
    sum = 0
    for x in input_list:
        sum += x
    return sum

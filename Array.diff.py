"""
Task:

Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
It should remove all values from list a, which are present in list b keeping their order.

Examples:

array_diff([1,2],[1]) == [2]
array_diff([1,2,2,2,3],[2]) == [1,3]

Solution:
"""


def array_diff(a, b):
    return [x for x in a if x not in b]
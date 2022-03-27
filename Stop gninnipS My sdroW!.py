"""
Task:

Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
It should remove all values from list a, which are present in list b keeping their order.

Examples:

array_diff([1,2],[1]) == [2]
array_diff([1,2,2,2,3],[2]) == [1,3]

Solution:
"""


def spin_words(sentence):
    words = sentence.split(' ')
    new_words = [w[::-1] if len(w) >= 5 else w for w in words]
    return ' '.join(new_words)


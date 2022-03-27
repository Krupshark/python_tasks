"""
Task:

Your task is to create a new implementation of modpow so that it computes (x^y)%n for large y.
The problem with the current implementation is that the output of Math.pow is so large on our inputs that it won't fit in a 64-bit float.
You're also going to need to be efficient, because we'll be testing some pretty big numbers.

A lot of things have been forbidden. Amidst others, don't:

1)import things
2)use eval, exec, compile, ... and a lot of things you'd use to cheat your way through the kata
3)use the int.__pow__ method
Due to these limitations, you cannot use any property or method (like, even lst.append is forbidden).


Solution:
"""


def power_mod(x, y, n):
    number = 1
    while y:
        if y & 1:
            number = number * x % n
        y >>= 1
        x = x * x % n
    return number

#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def count(i, n):
    x = n // i
    pass


def eating_cookies(n, cache=None):
    total_steps = 0
    steps1 = 0
    steps2 = 0
    steps3 = 0
    for i in range(1, 4):
        count(i, n)
    pass


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')

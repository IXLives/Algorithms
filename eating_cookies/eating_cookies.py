#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution
# permutation questions = 'possible ways'

cache = {}


def eating_cookies(n, cache=None):
    if cache and n in cache:
        return cache[n]
    # base case, no more cookies
    if n == 0:
        if cache != None:
            cache[n] = 1
        return 1
    total_ways = 0
    # 3 cookies, eat them all
    if n >= 3:
        total_ways += eating_cookies(n - 3, cache)
        if cache != None:
            cache[n] = total_ways
    # 2 cookies, eat them all
    if n >= 2:
        total_ways += eating_cookies(n - 2, cache)
        if cache != None:
            cache[n] = total_ways
    # 1 cookie, eat IT
    if n >= 1:
        total_ways += eating_cookies(n - 1, cache)
        if cache != None:
            cache[n] = total_ways
    return total_ways


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies, cache), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')

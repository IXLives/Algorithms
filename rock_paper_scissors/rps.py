#!/usr/bin/python

import sys


def memoize(function):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = function(x)
        return memo[x]
    return helper


def rock_paper_scissors(n):
    plays = ['rock', 'paper', 'scissors']
    cache = []
    all_plays = []

    def find_plays(play, round_number, cache):
        for i in range(0, len(plays)):
            play.append(plays[i])
            if round_number == n and play not in all_plays:
                all_plays.extend(play)
            else:
                find_plays(play, round_number + 1, cache)

    find_plays([], 1, cache)

    return all_plays


rock_paper_scissors = memoize(rock_paper_scissors)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')

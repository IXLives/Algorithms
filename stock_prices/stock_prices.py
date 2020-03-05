#!/usr/bin/python

import argparse


def find_max_profit(prices):
    maxprofit = -100
    current_price = prices[0]
    current_profit = -100
    lowest_price = prices[0]

    for i in range(1, len(prices) - 1):
        current_price = prices[i]
        if current_price < lowest_price:
            lowest_price = current_price
        current_profit = prices[i] - lowest_price

        if current_profit > maxprofit:
            maxprofit = current_profit
    return maxprofit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))

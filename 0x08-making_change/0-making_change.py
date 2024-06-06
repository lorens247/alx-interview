#!/usr/bin/python3
'''
Making Change Algorithm
'''


def makeChange(coins, total):
    '''
    Determine the fewest number of coins needed to meeta given
    amount total from a pile of coins of different values.
    '''

    if total <= 0:
        return 0

    else:
        dp = sorted(coins)
        dp.reverse()
        dp_count = 0
        for i in dp:
            while (total >= i):
                dp_count += 1
                total -= i
        if total == 0:
            return dp_count
        return -1

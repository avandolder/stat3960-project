#!/usr/bin/env python3

# STAT-3980 Project
# Author: Adam Vandolder, Student #104629080

import argparse
import random

def next_price(curr_price):
    """Generate the next day's stock price from the current price."""
    if curr_price <= 9:
        if random.random() <= (curr_price - 4) / 10:
            return curr_price - 1
        else:
            return curr_price + 1
    else:
        if random.random() <= (14 - curr_price) / 10:
            return curr_price + 1
        else:
            return curr_price - 1

def profit_from_trial(days, initial_price):
    """Compute profit from a trial using the strategy, given days and initial_price."""
    price = initial_price
    shares = 0.0
    
    for day in range(days):
        shares += 1000 / price
        price = next_price(price)

    return shares * price - 1000 * days

def run_trials(trials, days, price, quiet):
    """Run trials and output average profit/loss."""
    profits = [profit_from_trial(days, price) for i in range(trials)]

    if not quiet:
        print('Profit/Loss from {} Trials'.format(trials))
        for (i, profit) in enumerate(profits):
            print('Trial #{}:\t${:>10.2f}'.format(i + 1, profit))
        print()

    print('Average Profit:\t${:>10.2f}'.format(sum(profits) / len(profits)))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Compute average profit from a number of trials')
    parser.add_argument('-t', '--trials', type=int, help='Number of trials to run', default=20)
    parser.add_argument('-d', '--days', type=int, help='Number of days to run each trial', default=70)
    parser.add_argument('-p', '--price', type=int, help='Initial stock price', default=9)
    parser.add_argument('-q', '--quiet', action='store_true', help='Only output average profit')
    run_trials(**vars(parser.parse_args()))

import random
import sys

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

def simulate(days, initial_price):
    """Simulate profit from running the strategy with specified days and initial_price."""
    price = initial_price
    stocks = 0
    
    for day in range(days):
        stocks += 1000 / price
        price = next_price(price)

    return stocks * price - 1000 * days

def main(args):
    simulations = [simulate(days=70, initial_price=9) for i in range(20)]

    print('Profit/Loss from 20 Simulations')
    for (i, profit) in enumerate(simulations):
        print('Simulation {}:\t${:>10.2f}'.format(i + 1, profit))

    print('\nAverage Profit:\t${:>10.2f}'.format(sum(simulations) / len(simulations)))

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))

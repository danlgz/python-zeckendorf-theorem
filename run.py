import argparse
from zeckendorf import zeckendorf

parser = argparse.ArgumentParser(description='Zeckendorf\'s theorem')

parser.add_argument('--input', help='Number to generate the Zeckendorf decomposition')

args = parser.parse_args()

if args.input:
    try:
        n = abs(int(args.input))
        print('')
        print('result: {}'.format(zeckendorf(n)))
        print('')
    except:
        print('Please, enter a natural number')

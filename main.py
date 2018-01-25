import random
import argparse
import logging as log
from random import randint as ri
from score import score
from util import mkdir


# Runs scoring function and checks if score is improved.
def process(out, seed):
    sc = score(inp, out)

    with open(args.testcase + '.max', 'r') as f:
        bsc = int(f.readline())

    fmt = 'Score: {:<20} Testcase: {}'
    if sc > bsc:
        log.critical(fmt.format(sc + " BEST", args.testcase))
        fname = '_'.join([args.testcase, str(sc), seed]) + '.ans'

        with open(args.testcase + '.max', 'w') as f:
            f.write(str(sc))

        mkdir('ans')
        with open('ans/' + fname, 'w') as f:
            # Print to f
            f.write(str(out))
    else:
        log.warn(fmt.format(sc, args.testcase))


def greedy(seed):
    # TODO: Solve the problem
    random.seed(seed)

    process(0, seed)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('testcase')
    parser.add_argument('-l', '--log', default='debug')
    parser.add_argument('-s', '--seed', default=None)
    parser.add_argument('-n', '--iterations', default=10)
    return parser.parse_args()


def init_log():
    loglvls = {'debug': log.DEBUG, 'info': log.INFO, 'warning': log.WARNING, 'error': log.ERROR, 'critical': log.CRITICAL}
    logfmt = '%(relativeCreated)6d %(message)s'
    log.basicConfig(level=loglvls[args.log], format=logfmt)


if __name__ == '__main__':
    args = get_args()
    init_log()

    with open('in/' + args.testcase + '.in') as f:
        inp = f.read()
        # TODO: Proccess input data

    if args.seed:
        log.info('seed: {}'.format(args.seed))
        greedy(args.seed)
    else:
        for i in range(args.iterations):
            seed = ri(0, 10000)
            log.info('seed: {}, test#: {}'.format(seed, i))
            greedy(seed)

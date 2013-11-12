__author__ = 'flaviocaetano'

from datetime import datetime

from problem_12.solution import divisor_generator


def divisors(x):
    for i in xrange(1, int(x/2)+1):
        if x % i == 0:
            yield i


def d(x):
    divisor_set = set(divisor_generator(x)) - set([x])
    return sum(divisor_set)



if __name__ == '__main__':
    t0 = datetime.now()

    result_set = set()

    for target in xrange(1, 10000):
        d_target = d(target)
        if target != d_target and d(d_target) == target:
            result_set |= set([target, d_target])

    result = sum(result_set)

    t1 = datetime.now() - t0

    print 'result: %s (%ss)' % (result, t1)

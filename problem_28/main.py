__author__ = 'flaviocaetano'

from datetime import datetime


def sum_spiral(limit):
    i = 1
    last_threshold = 2
    threshold_count = 0

    sum = 0
    while i < limit:
        sum += i
        if threshold_count == 4:
            last_threshold += 2
            threshold_count = 0

        i += last_threshold
        threshold_count += 1

    return sum


if __name__ == '__main__':
    t0 = datetime.now()

    result = sum_spiral(1001**2+1)

    t1 = datetime.now() - t0

    print 'result: %s (%ss)' % (result, t1)

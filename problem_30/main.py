__author__ = 'flaviocaetano'

from datetime import datetime


def calc_pow(pow):
    for i in range(2, 10**6):
        sum_i = 0
        for letter in str(i):
            sum_i += int(letter) ** pow

        if sum_i == i:
            yield i


if __name__ == '__main__':
    t0 = datetime.now()

    result = sum(calc_pow(5))

    t1 = datetime.now() - t0

    print 'result: %s (%ss)' % (result, t1)

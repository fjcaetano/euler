__author__ = 'flaviocaetano'

from datetime import datetime

from problem_3.main import gen_primes


if __name__ == '__main__':
    t0 = datetime.now()

    pow_str = str(2**1000)
    result = sum(map(int, pow_str))

    t1 = datetime.now() - t0

    print 'result: %s (%ss)' % (result, t1)

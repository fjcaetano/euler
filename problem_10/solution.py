__author__ = 'flaviocaetano'

from datetime import datetime

from problem_3.main import gen_primes


if __name__ == '__main__':
    t0 = datetime.now()

    result = sum(gen_primes(2*10**6))

    t1 = datetime.now() - t0

    print 'result: %s (%ss)' % (result, t1)

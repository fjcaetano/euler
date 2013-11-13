__author__ = 'flaviocaetano'

from datetime import datetime

from problem_5.main import factors


quadratic = lambda n, a, b: n**2 + a*n + b


def main():
    result = (0, 0, 0)

    for a in range(-999, 1000):
        for b in range(-999, 1000):
            n = 0
            while len(factors(abs(quadratic(n, a, b)))) == 1:
                n += 1

            if n > result[0]:
                result = (n, a, b)
                print result

    return result


if __name__ == '__main__':
    t0 = datetime.now()

    result = main()

    t1 = datetime.now() - t0

    print 'result: %s (%ss)' % (result, t1)

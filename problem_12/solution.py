__author__ = 'flaviocaetano'

from datetime import datetime


def nth_triangle(n):
    return sum(range(1, n+1))


def divisor_generator(n):
    sqrt = lambda x: int(x**0.5)

    for i in xrange(1,sqrt(n)+1):
        if n%i == 0:
            yield i;
            yield n/i;


if __name__ == '__main__':
    t0 = datetime.now()

    i = 1
    result = None
    div_list = list()

    while len(div_list) < 500:
        result = nth_triangle(i)
        div_list = list(divisor_generator(result))

        i += 1

    t1 = datetime.now() - t0

    print 'result: %s (%ss)' % (result, t1)

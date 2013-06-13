__author__ = 'flaviocaetano'

from datetime import datetime


odd = lambda x: 3*x + 1
even = lambda x: x/2


def chain(num):
    yield num

    while num > 1:
        num = even(num) if num % 2 == 0 else odd (num)
        yield num


if __name__ == "__main__":
    t0 = datetime.now()

    result = None
    max_len = -1

    for num in range(1, 10**6):
        new_len = len(list(chain(num)))
        if new_len > max_len:
            max_len = new_len
            result = num

    t1 = datetime.now() - t0

    print 'result : %s - %s (%ss)' % (result, max_len, t1)

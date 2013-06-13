__author__ = 'flaviocaetano'

from datetime import datetime


if __name__ == '__main__':
    t0 = datetime.now()

    result = 0

    with open('number.txt', 'r') as numbers_txt:
        for line in numbers_txt.readlines():
            result += int(line[:11])

    result = str(result)[:10]

    t1 = datetime.now() - t0

    print 'result: %s (%ss)' % (result, t1)

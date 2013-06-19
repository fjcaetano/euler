__author__ = 'flaviocaetano'

from datetime import datetime

from num2eng import num2eng


if __name__ == '__main__':
    t0 = datetime.now()

    result = 0
    for i in range(1000):
        word = num2eng(i+1)
        print word
        result += len(word.replace(' ', ''))

    t1 = datetime.now() - t0

    print 'result: %s (%ss)' % (result, t1)

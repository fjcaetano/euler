__author__ = 'flaviocaetano'

from datetime import datetime


def mult_pythagorean(num):
    '''
    Find the multiplication of the pythagorean numbers which sum is num.
    '''

    for a in range(2, num):
        for b in range(2, num+1):
            c = num - a - b
            if a+b+c == 1000 and a**2+b**2 == c**2:
                return a*b*c


if __name__ == '__main__':
    t0 = datetime.now()

    result = mult_pythagorean(1000)

    t1 = datetime.now() - t0

    print 'result: %s (%ss)' % (result, t1)

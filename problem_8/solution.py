__author__ = 'flaviocaetano'

from datetime import datetime


def mult_consecutives(str_number, length):
    '''
    Find the greatest product of the given lenght's consecutive digits in the given str_number.
    '''

    result = -1
    start = 0

    consecutive  = str_number[start:length]
    while start+length < len(str_number):

        mult = reduce(lambda x, y: x*y, [int(i) for i in consecutive])
        result = max(mult, result)

        start += 1
        consecutive = str_number[start:length+start]

    return result


if __name__ == '__main__':
    t0 = datetime.now()

    result = None
    with open('number.txt', 'r') as file:
        str_number = file.read()

        result = mult_consecutives(str_number, 5)

    t1 = datetime.now() - t0

    print 'result: %s (%ss)' % (result, t1)
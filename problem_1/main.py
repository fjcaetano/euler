__author__ = 'Flavio'


def sum_multiples_of_3_and_5(param):
    '''
    Sum all multiples of 3 and 5 below the given number.
    '''

    i = 1
    result = 0
    while i < param:

        if i % 3 == 0:
            result += i

        elif i % 5 == 0:
            result += i

        i += 1

    return result

if __name__ == '__main__':
    print sum_multiples_of_3_and_5(1000)

__author__ = 'Flavio'

import sys
import os
import datetime
# Add the ptdraft folder path to the sys.path list
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..'))

from problem_3.main import gen_primes


def factors(number):
    '''
    Returns a list with the number's factors
    '''

    prime_list = list(gen_primes(number+1))
    result = list()

    while number > 1:
        for prime in sorted(prime_list):
            if number % prime == 0:
                result.append(prime)
                number /= prime
            else:
                prime_list.remove(prime)

    return result


def smallest_divisible_all(number):
    '''
    Find the smallest number divisable by all numbers <= number
    '''

    i = number
    result = 1

    factor_list = list()

    while i > 0:
        number = i

        for fac in factor_list:
            if number % fac == 0:
                number /= fac

        result *= number

        factor_list += factors(number)

        i -= 1

    return result


if __name__ == '__main__':
    t0 = datetime.datetime.now()

    result = smallest_divisible_all(20)

    t1 = datetime.datetime.now() - t0

    print 'result: %d (%ss)' % (result, t1,)
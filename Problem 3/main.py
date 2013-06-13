__author__ = 'Flavio'

import datetime


def gen_primes(number):
    """
    Genereates a list with all primes below the given number

    http://stackoverflow.com/a/568618
    """
    composites = {}
    prime = 2

    while prime < number:
        if prime not in composites:
            yield prime

            composites[prime * prime] = [prime]
        else:
            for p in composites[prime]:
                composites.setdefault(p + prime, []).append(p)

            del composites[prime]

        prime += 1


def largest_prime_factor(number):
    '''
    Returns the largest prime factor
    '''

    prime_list = gen_primes(number ** 0.5)
    for prime in reversed(list(prime_list)):
        if number % prime == 0:
            return prime


if __name__ == '__main__':
    t0 = datetime.datetime.now()

    result = largest_prime_factor(600851475143)

    t1 = datetime.datetime.now() - t0

    print 'result: %d (%ss)' % (result, t1,)
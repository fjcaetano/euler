__author__ = 'flaviocaetano'

from datetime import datetime


def gen_primes(number):
    """
    Generates the nth prime number

    http://stackoverflow.com/a/568618
    """
    composites = {}
    prime = 2
    result = []

    while len(result) < number:
        if prime not in composites:
            result.append(prime)

            composites[prime * prime] = [prime]
        else:
            for p in composites[prime]:
                composites.setdefault(p + prime, []).append(p)

            del composites[prime]

        prime += 1

    return result.pop()


if __name__ == '__main__':
    t0 = datetime.now()

    result = gen_primes(10001)

    t1 = datetime.now() - t0

    print 'result: %s (%ss)' % (result, t1)

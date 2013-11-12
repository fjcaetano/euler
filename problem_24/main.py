__author__ = 'flaviocaetano'

from datetime import datetime
from itertools import permutations


def main(n_th, digits):
    perm_list = permutations(digits)
    sorted_perm_list = sorted(perm_list)

    return ''.join(sorted_perm_list[n_th-1])


if __name__ == '__main__':
    t0 = datetime.now()

    result = main(1000000, '0123456789')

    t1 = datetime.now() - t0

    print 'result: %s (%ss)' % (result, t1)

__author__ = 'Flavio'

from datetime import datetime


def largest_palindrome(*nums):
    '''
    '''

    palindrome = -1

    while max(nums) > 100:
        n1 = max(nums)
        n2 = min(nums)

        num = n1 * n2
        num_str = str(num)

        if num_str == num_str[::-1]:
            if num > palindrome:
                palindrome = num

        if n2-1 < 100:
            n1 -=1
            n2 = n1

        nums = [n1, n2-1]

    return palindrome


if __name__ == '__main__':
    t0 = datetime.now()

    pal = largest_palindrome(999, 999)

    t1 = datetime.now() - t0

    print 'result: %d (%ss)' % (pal, t1)
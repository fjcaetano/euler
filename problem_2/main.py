__author__ = 'Flavio'


def sum_even_fibo(limit):
    '''
    Sum all even numbers in Fibonacci sequence less than limit
    '''

    nm1 = 1
    nth = 0

    result = 0

    while nth < limit:
        if nth % 2 == 0:
            result += nth

        nth += nm1
        nm1 = nth - nm1

    return result

if __name__ == '__main__':
    print sum_even_fibo(4*10**6)

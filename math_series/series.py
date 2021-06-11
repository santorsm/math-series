def fibonacci(n):
    """Using recusion - takes in a number n, returns the nth value of the fibonacci sequence"""

    # positions 0 and 1 are 0 and 1
    if n < 2:
        return n
    # for all others add the fibonacci numbers from the 2 previous positions
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fib_iterate(n):
    """Using iteration - takes in a number n, returns the nth value of the fibonacci sequence"""
    # unfortunately I couldn't figure it out myself so I found a way to do this iteratively https://pythonistaplanet.com/fibonacci-sequence-iterative/
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a


def lucas(n):
    """Using recusion - takes in a number n, returns the nth value of the lucas sequence"""

    # positions 0 and 1 are 2 and 1
    if n == 0:
        return 2
    if n == 1:
        return 1
    # for all others add the fibonacci numbers from the 2 previous positions
    else:
        return lucas(n - 1) + lucas(n - 2)


# def sum_series(n, first=0, second=1):

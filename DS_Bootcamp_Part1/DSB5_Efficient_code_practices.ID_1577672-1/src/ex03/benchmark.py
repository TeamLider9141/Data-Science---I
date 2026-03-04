import sys
import timeit
from functools import reduce


def sum_squares_loop(n):
    total = 0
    for i in range(1, n + 1):
        total += i * i
    return total


def sum_squares_reduce(n):
    return reduce(lambda acc, x: acc + x * x, range(1, n + 1), 0)


def benchmark(method_name, calls, n):
    methods = {
        'loop': sum_squares_loop,
        'reduce': sum_squares_reduce
    }

    if method_name not in methods:
        raise Exception("Unknown method")

    func = methods[method_name]

    return timeit.timeit(
        lambda: func(n),
        number=calls
    )


def main():
    if len(sys.argv) != 4:
        return

    method = sys.argv[1]
    calls = int(sys.argv[2])
    n = int(sys.argv[3])

    result = benchmark(method, calls, n)
    print(result)


if __name__ == '__main__':
    main()

import timeit
import random
from collections import Counter


def generate_list():
    return [random.randint(0, 100) for _ in range(1_000_000)]


def my_count(data):
    result = {}
    for num in data:
        result[num] = result.get(num, 0) + 1
    return result


def counter_count(data):
    return Counter(data)


def my_top(data):
    counts = my_count(data)
    return sorted(counts.items(), key=lambda x: x[1], reverse=True)[:10]


def counter_top(data):
    return Counter(data).most_common(10)


def benchmark():
    data = generate_list()

    my_count_time = timeit.timeit(
        lambda: my_count(data),
        number=1
    )

    counter_count_time = timeit.timeit(
        lambda: counter_count(data),
        number=1
    )

    my_top_time = timeit.timeit(
        lambda: my_top(data),
        number=1
    )

    counter_top_time = timeit.timeit(
        lambda: counter_top(data),
        number=1
    )

    print(f"my function: {my_count_time}")
    print(f"Counter: {counter_count_time}")
    print(f"my top: {my_top_time}")
    print(f"Counter's top: {counter_top_time}")


def main():
    benchmark()


if __name__ == '__main__':
    main()

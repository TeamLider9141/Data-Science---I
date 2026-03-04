import timeit
import sys


def get_emails():
    return [
        'john@gmail.com',
        'james@gmail.com',
        'alice@yahoo.com',
        'anna@live.com',
        'philipp@gmail.com'
    ] * 5


def loop(emails):
    result = []
    for email in emails:
        if email.endswith('@gmail.com'):
            result.append(email)
    return result


def list_comprehension(emails):
    return [email for email in emails if email.endswith('@gmail.com')]


def map_method(emails):
    def check(email):
        return email if email.endswith('@gmail.com') else None
    return list(filter(None, map(check, emails)))


def filter_method(emails):
    return list(filter(lambda email: email.endswith('@gmail.com'), emails))


def benchmark(method_name, calls):
    methods = {
        'loop': loop,
        'list_comprehension': list_comprehension,
        'map': map_method,
        'filter': filter_method
    }

    if method_name not in methods:
        raise Exception("Unknown method")

    emails = get_emails()
    func = methods[method_name]

    return timeit.timeit(
        lambda: func(emails),
        number=calls
    )


def main():
    if len(sys.argv) != 3:
        return

    method_name = sys.argv[1]
    calls = int(sys.argv[2])

    result = benchmark(method_name, calls)
    print(result)


if __name__ == '__main__':
    main()

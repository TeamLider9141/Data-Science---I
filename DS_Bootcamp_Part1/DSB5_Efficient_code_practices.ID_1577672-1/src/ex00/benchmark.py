import timeit


def get_gmail_loop(emails):
    result = []
    for email in emails:
        if email.endswith('@gmail.com'):
            result.append(email)
    return result


def get_gmail_comprehension(emails):
    return [email for email in emails if email.endswith('@gmail.com')]


def benchmark():
    emails = [
        'john@gmail.com',
        'james@gmail.com',
        'alice@yahoo.com',
        'anna@live.com',
        'philipp@gmail.com'
    ] * 5

    loop_time = timeit.timeit(
        lambda: get_gmail_loop(emails),
        number=90_000_000
    )

    comp_time = timeit.timeit(
        lambda: get_gmail_comprehension(emails),
        number=90_000_000
    )

    if comp_time <= loop_time:
        print("it is better to use a list comprehension")
    else:
        print("it is better to use a loop")

    times = sorted([comp_time, loop_time])
    print(f"{times[0]} vs {times[1]}")


def main():
    benchmark()


if __name__ == '__main__':
    main()

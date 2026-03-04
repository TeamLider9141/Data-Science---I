import timeit


def get_gmail_loop(emails):
    result = []
    for email in emails:
        if email.endswith('@gmail.com'):
            result.append(email)
    return result


def get_gmail_comprehension(emails):
    return [email for email in emails if email.endswith('@gmail.com')]


def get_gmail_map(emails):
    def check_gmail(email):
        if email.endswith('@gmail.com'):
            return email
        return None

    return list(filter(None, map(check_gmail, emails)))


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

    map_time = timeit.timeit(
        lambda: get_gmail_map(emails),
        number=90_000_000
    )

    times = {
        "loop": loop_time,
        "comprehension": comp_time,
        "map": map_time
    }

    fastest = min(times, key=times.get)

    if fastest == "map":
        print("it is better to use a map")
    elif fastest == "comprehension":
        print("it is better to use a list comprehension")
    else:
        print("it is better to use a loop")

    sorted_times = sorted(times.values())
    print(f"{sorted_times[0]} vs {sorted_times[1]} vs {sorted_times[2]}")


def main():
    benchmark()


if __name__ == '__main__':
    main()

import sys

if sys.platform.startswith("win"):
    import os
    import psutil
else:
    import resource


def read_lines_generator(path):
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            yield line


def get_metrics():
    if sys.platform.startswith("win"):
        process = psutil.Process(os.getpid())
        mem = process.memory_info().peak_wset / (1024 ** 3)
        cpu = process.cpu_times()
        time_spent = cpu.user + cpu.system
    else:
        usage = resource.getrusage(resource.RUSAGE_SELF)
        mem = usage.ru_maxrss / (1024 ** 2)
        time_spent = usage.ru_utime + usage.ru_stime

    return mem, time_spent


def main():
    if len(sys.argv) != 2:
        raise Exception("Usage: generator.py <path_to_file>")

    path = sys.argv[1]

    for _ in read_lines_generator(path):
        pass

    mem, time_spent = get_metrics()

    print(f"Peak Memory Usage = {mem:.3f} GB")
    print(f"User Mode Time + System Mode Time = {time_spent:.2f}s")


if __name__ == '__main__':
    main()

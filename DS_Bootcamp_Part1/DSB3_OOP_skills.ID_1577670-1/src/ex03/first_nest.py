import sys
import os


class Research:
    def __init__(self, file_path):
        if not os.path.exists(file_path):
            raise Exception("File does not exist")
        self.file_path = file_path

    def file_reader(self, has_header=True):
        with open(self.file_path, 'r') as f:
            lines = f.read().strip().split('\n')

        if has_header:
            lines = lines[1:]

        data = []
        for line in lines:
            parts = line.split(',')
            if len(parts) != 2:
                raise Exception("Wrong file format")
            if parts not in [['0', '1'], ['1', '0']]:
                raise Exception("Wrong data values")
            data.append([int(parts[0]), int(parts[1])])

        return data

    class Calculations:
        def counts(self, data):
            heads = sum(row[0] for row in data)
            tails = sum(row[1] for row in data)
            return heads, tails

        def fractions(self, heads, tails):
            total = heads + tails
            return heads / total, tails / total


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise Exception("Wrong number of arguments")

    research = Research(sys.argv[1])
    data = research.file_reader()

    calc = research.Calculations()
    heads, tails = calc.counts(data)
    head_frac, tail_frac = calc.fractions(heads, tails)

    print(data)
    print(heads, tails)
    print(f"{head_frac:.4f} {tail_frac:.4f}")

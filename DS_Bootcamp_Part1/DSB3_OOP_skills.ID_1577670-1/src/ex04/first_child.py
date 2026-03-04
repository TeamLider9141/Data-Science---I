import sys
from random import randint

class Research:
    def __init__(self, file_path):

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except FileNotFoundError:
            raise Exception("File does not exist")


        self.data = []
        for line in lines[1:]:
            parts = line.strip().split(',')
            if len(parts) != 2:
                raise Exception("Incorrect file structure")
            self.data.append([int(parts[0]), int(parts[1])])

    def file_reader(self):
        return self.data


    class Calculations:
        def __init__(self, data):
            self.data = data

        def counts(self):
            heads = sum(row[0] for row in self.data)
            tails = sum(row[1] for row in self.data)
            return heads, tails

        def fractions(self, heads, tails):
            total = heads + tails
            return round(heads / total, 4), round(tails / total, 4)

class Analytics(Research.Calculations):
    def predict_random(self, n):
        result = []
        for _ in range(n):
            h = randint(0, 1)
            t = 1 - h
            result.append([h, t])
        return result

    def predict_last(self):
        return self.data[-1]



if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise Exception("Please provide exactly one file path as argument")

    research = Research(sys.argv[1])
    data = research.file_reader()
    print(data)

    calc = research.Calculations(data)
    heads, tails = calc.counts()
    print(heads, tails)

    frac_heads, frac_tails = calc.fractions(heads, tails)
    print(frac_heads, frac_tails)

    analytics = Analytics(data)
    print(analytics.predict_random(3))
    print(analytics.predict_last())

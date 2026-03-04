#to run it => python3 make_report.py data.csv

from random import randint

class Calculations:
    def __init__(self, data):
        self.data = data

    def counts(self):
        heads = sum(row[0] for row in self.data)
        tails = sum(row[1] for row in self.data)
        return heads, tails

    def fractions(self):
        heads, tails = self.counts()
        total = heads + tails
        return heads/total, tails/total

class Analytics(Calculations):
    def __init__(self, data):
        super().__init__(data)

    def predict_random(self, steps):
        result = []
        for _ in range(steps):
            flip = [1, 0] if randint(0,1) else [0, 1]
            result.append(flip)
        return result

    def predict_last(self):
        return self.data[-1]

    def save_file(self, data, file_name, extension='txt'):
        with open(f"{file_name}.{extension}", 'w', encoding='utf-8') as f:
            f.write(data)

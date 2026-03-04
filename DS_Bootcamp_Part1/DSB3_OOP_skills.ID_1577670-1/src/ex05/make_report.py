

#to run it => python3 make_report.py data.csv

import sys
from analytics import Analytics
from config import num_of_steps, report_template

def file_reader(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        next(f)  # header
        data = [[int(line.strip().split(',')[0]), int(line.strip().split(',')[1])] for line in f]
    return data

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise Exception("Please provide the path to the data file.")

    data_file = sys.argv[1]
    data = file_reader(data_file)

    analytics = Analytics(data)

    heads, tails = analytics.counts()
    heads_percent, tails_percent = analytics.fractions()
    future = analytics.predict_random(num_of_steps)

    future_heads = sum(f[0] for f in future)
    future_tails = sum(f[1] for f in future)

    report = report_template.format(
        total = heads + tails,
        heads = heads,
        tails = tails,
        heads_percent = heads_percent*100,
        tails_percent = tails_percent*100,
        steps = num_of_steps,
        future_heads = future_heads,
        future_tails = future_tails
    )

    print(report)
    analytics.save_file(report, "coin_report")

#to run it => python3 make_report.py data.csv

num_of_steps = 3

report_template = """Report:
We made {total} observations by tossing a coin: {tails} were tails and {heads} were heads. 
The probabilities are {tails_percent:.2f}% and {heads_percent:.2f}%, respectively. 
Our forecast is that the next {steps} observations will be: {future_tails} tail(s) and {future_heads} head(s)."""

import sys


def all_stocks():
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }

    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }

    if len(sys.argv) != 2:
        return

    raw_input = sys.argv[1]
    expressions = raw_input.split(',')

    cleaned = []

    for expr in expressions:
        expr = expr.strip()
        if not expr:
            return
        cleaned.append(expr)

    for expr in cleaned:
        # ticker check
        ticker = expr.upper()
        company = expr.capitalize()

        if ticker in STOCKS:
            for name, tick in COMPANIES.items():
                if tick == ticker:
                    print(f"{ticker} is a ticker symbol for {name}")
                    break

        elif company in COMPANIES:
            tick = COMPANIES[company]
            price = STOCKS[tick]
            print(f"{company} stock price is {price}")

        else:
            print(f"{expr} is an unknown company or an unknown ticker symbol")


if __name__ == '__main__':
    all_stocks()


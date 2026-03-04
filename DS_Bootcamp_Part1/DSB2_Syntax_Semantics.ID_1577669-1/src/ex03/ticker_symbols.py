import sys


def ticker_lookup():
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

    ticker_input = sys.argv[1].upper()

    if ticker_input in STOCKS:
        price = STOCKS[ticker_input]

        # reverse search
        for company, ticker in COMPANIES.items():
            if ticker == ticker_input:
                print(company, price)
                return
    else:
        print("Unknown ticker")


if __name__ == '__main__':
    ticker_lookup()

    #test versiya => 
    # python3 ticker_symbols.py tsla  => natija esa => Tesla 724.88



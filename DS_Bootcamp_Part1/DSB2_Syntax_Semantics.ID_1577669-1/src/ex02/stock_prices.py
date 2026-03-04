import sys


def stock_lookup():
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

    # Faqat 1 ta argument bo‘lishi kerak
    if len(sys.argv) != 2:
        return

    company_input = sys.argv[1].capitalize()

    if company_input in COMPANIES:
        ticker = COMPANIES[company_input]
        print(STOCKS[ticker])
    else:
        print("Unknown company")


if __name__ == '__main__':
    stock_lookup()

   #python3 stock_prices.py tesla => natija esa 724.88

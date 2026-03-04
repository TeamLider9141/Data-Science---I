#!/usr/bin/env python3

import sys
import time
import requests
from bs4 import BeautifulSoup


def fetch_page(ticker):
    url = f"https://finance.yahoo.com/quote/{ticker}/financials"

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/122.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9",
    }

    session = requests.Session()

    response = session.get(url, headers=headers, timeout=10)

    if response.status_code != 200:
        raise Exception("URL does not exist")

    return response.text


def parse_financials(html, field):
    soup = BeautifulSoup(html, "html.parser")

    # Yahoo finance rows
    rows = soup.find_all("div", attrs={"data-test": "fin-row"})

    if not rows:
        raise Exception("Requested field does not exist")

    for row in rows:
        title = row.find("div")

        if not title:
            continue

        name = title.get_text(strip=True)

        if name == field:
            values = [field]

            columns = row.find_all("div")[1:]
            for col in columns:
                text = col.get_text(strip=True)
                if text:
                    values.append(text)

            if len(values) == 1:
                raise Exception("Requested field does not exist")

            return tuple(values)

    raise Exception("Requested field does not exist")


def main():
    if len(sys.argv) != 3:
        raise Exception("Invalid arguments")

    ticker = sys.argv[1]
    field = sys.argv[2]

    time.sleep(5)

    html = fetch_page(ticker)
    result = parse_financials(html, field)

    print(result)


if __name__ == "__main__":
    main()

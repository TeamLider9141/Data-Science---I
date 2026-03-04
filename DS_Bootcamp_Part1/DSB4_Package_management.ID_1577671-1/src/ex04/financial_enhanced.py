import urllib.request

def fetch_page(ticker):
    url = f"https://finance.yahoo.com/quote/{ticker}/financials"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0"}
    )
    with urllib.request.urlopen(req) as response:
        if response.status != 200:
            raise Exception("URL does not exist")
        return response.read().decode()

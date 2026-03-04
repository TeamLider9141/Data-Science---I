import logging
import requests
from random import randint
import config

logging.basicConfig(
    filename=config.LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s %(message)s"
)


class Research:

    def __init__(self, path):
        logging.info("Initializing Research class")
        self.path = path

    def file_reader(self, has_header=True):
        logging.info("Reading data file")
        with open(self.path, "r") as file:
            lines = file.read().strip().split("\n")

        if has_header:
            lines = lines[1:]

        data = [[int(x) for x in line.split(",")] for line in lines]
        return data

    def send_telegram_message(self, message):
        logging.info("Sending Telegram notification")
        if not config.TELEGRAM_TOKEN or not config.TELEGRAM_CHAT_ID:
            logging.warning("Telegram credentials not set")
            return

        url = f"https://api.telegram.org/bot{config.TELEGRAM_TOKEN}/sendMessage"
        payload = {
            "chat_id": config.TELEGRAM_CHAT_ID,
            "text": message
        }

        requests.post(url, json=payload)


class Calculations:

    def __init__(self, data):
        logging.info("Initializing Calculations class")
        self.data = data

    def counts(self):
        logging.info("Calculating counts")
        heads = sum(1 for row in self.data if row == [0, 1])
        tails = sum(1 for row in self.data if row == [1, 0])
        return heads, tails

    def fractions(self):
        logging.info("Calculating fractions")
        heads, tails = self.counts()
        total = heads + tails
        return round(heads / total * 100, 2), round(tails / total * 100, 2)


class Analytics(Calculations):

    def predict_random(self, steps):
        logging.info("Generating random predictions")
        result = []
        for _ in range(steps):
            head = randint(0, 1)
            result.append([head, 1 - head])
        return result

    def predict_last(self):
        logging.info("Getting last observation")
        return self.data[-1]

    def save_file(self, data, filename, extension):
        logging.info("Saving report to file")
        with open(f"{filename}.{extension}", "w") as file:
            file.write(data)

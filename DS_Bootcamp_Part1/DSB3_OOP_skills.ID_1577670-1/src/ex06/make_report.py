#python3 make_report.py data.csv

from analytics import Research, Analytics
import config
import sys


if __name__ == "__main__":

    research = None

    try:
        if len(sys.argv) != 2:
            raise Exception("Provide data file path")

        path = sys.argv[1]

        research = Research(path)
        data = research.file_reader()

        analytics = Analytics(data)

        heads, tails = analytics.counts()
        head_frac, tail_frac = analytics.fractions()
        total = heads + tails

        predictions = analytics.predict_random(config.NUM_OF_STEPS)

        pred_heads = sum(1 for row in predictions if row == [0, 1])
        pred_tails = sum(1 for row in predictions if row == [1, 0])

        forecast = f"{pred_tails} tails and {pred_heads} heads"

        report = config.REPORT_TEMPLATE.format(
            total=total,
            tails=tails,
            heads=heads,
            tail_frac=tail_frac,
            head_frac=head_frac,
            steps=config.NUM_OF_STEPS,
            forecast=forecast
        )

        analytics.save_file(report, "report", "txt")

        research.send_telegram_message(
            "The report has been successfully created"
        )

        print(report)

    except Exception:

        if research:
            research.send_telegram_message(
                "The report hasn't been created due to an error."
            )

        raise

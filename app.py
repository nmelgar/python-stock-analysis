from flask import Flask, render_template, request
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    stock_info = {}
    chart_paths = {}
    summary_table = None

    if request.method == "POST":
        symbol = request.form["symbol"].upper()
        start_date = request.form["start_date"]
        end_date = request.form["end_date"]

        try:
            ticker = yf.Ticker(symbol)
            info = ticker.info

            stock_info = {
                "symbol": symbol,
                "name": info.get("shortName", "N/A"),
                "market": info.get("market", "N/A"),
                "sector": info.get("sector", "N/A"),
            }

            data = ticker.history(start=start_date, end=end_date)

            if not data.empty:
                data["20_Day_MA"] = data["Close"].rolling(window=20).mean()
                data["Daily_Return"] = data["Close"].pct_change() * 100

                # plot 1: close & moving average
                plt.figure(figsize=(10, 5))
                plt.plot(data["Close"], label="Close Price")
                plt.plot(data["20_Day_MA"], label="20-Day MA", linestyle="--")
                plt.title(f"{symbol} Closing Price & 20-Day MA")
                plt.xlabel("Date")
                plt.ylabel("Price")
                plt.legend()
                plt.grid()
                close_chart_path = f"static/close_{symbol}.png"
                plt.savefig(close_chart_path)
                plt.close()

                # plot 2: daily returns
                plt.figure(figsize=(10, 5))
                plt.plot(data["Daily_Return"], color="purple")
                plt.title(f"{symbol} Daily Returns")
                plt.xlabel("Date")
                plt.ylabel("Return (%)")
                plt.grid()
                return_chart_path = f"static/returns_{symbol}.png"
                plt.savefig(return_chart_path)
                plt.close()

                chart_paths = {
                    "close_chart": close_chart_path,
                    "returns_chart": return_chart_path,
                }

                # create summary table 1st and last 5 rows)
                summary_data = pd.concat([data.head(), data.tail()])
                summary_data = summary_data.round(2)
                summary_table = summary_data.to_html(classes="data-table", border=0)

            else:
                stock_info["error"] = "No data available for selected date range."

        except Exception as e:
            stock_info["error"] = f"Error fetching data: {e}"

    return render_template(
        "index.html",
        stock_info=stock_info,
        chart_paths=chart_paths,
        summary_table=summary_table,
    )


if __name__ == "__main__":
    os.makedirs("static", exist_ok=True)
    app.run(debug=True)

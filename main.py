# %%
# imports
import yfinance as yf
import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt

# %%
# df link
df_link = "https://raw.githubusercontent.com/nmelgar/tickers-web-scrap-python/refs/heads/main/stock_tickers_data.json"
df = pd.read_json(df_link)
# print(df.to_string())

# %%
# first col
symbol_col = df["symbol"]
print(symbol_col.count())

# %%
# check if symbol existand display basic stock info
symbol = input("Enter a symbol to analyze: ").upper()

if symbol in symbol_col.values:
    ticker_details = yf.Ticker(symbol)
    info = ticker_details.info
    print(f"Symbol: {symbol}")
    print(f"Name: {info.get('shortName', 'N/A')}")
    print(f"Market: {info.get('market', 'N/A')}")
    print(f"Sector: {info.get('sector', 'N/A')}")

    start_date = "2022-02-28"
    end_date = "2025-02-28"

    stock = yf.Ticker(symbol)
    historical_data = stock.history(start=start_date, end=end_date)

    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", None)

    print(f"Historical Data for {symbol} from {start_date} to {end_date}")

    formatted_data = pd.concat([historical_data.head(), historical_data.tail()])
    print(tabulate(formatted_data, headers="keys", tablefmt="psql"))

    print("\nShowing only the first and last 5 rows of data:")
    print(tabulate(formatted_data, headers="keys", tablefmt="grid"))

else:
    print("Please enter a valid symbol :)")

# %%
data = stock.history(start=start_date, end=end_date)
# calculate 20-day moving average
data["20_Day_MA"] = data["Close"].rolling(window=20).mean()

# calculate daily returns
data["Daily_Return"] = data["Close"].pct_change() * 100

# plot closing price and 20-day moving average
plt.figure(figsize=(12, 6))
plt.plot(data["Close"], label="Close Price", color="blue")
plt.plot(data["20_Day_MA"], label="20-Day Moving Average", color="orange")
plt.title(f"{symbol} Closing Price and 20-Day Moving Average")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plt.show()

# plot daily returns
plt.figure(figsize=(12, 6))
plt.plot(data["Daily_Return"], label="Daily Returns", color="purple")
plt.title(f"{symbol} Daily Returns")
plt.xlabel("Date")
plt.ylabel("Daily Return (%)")
plt.legend()
plt.grid(True)
plt.show()
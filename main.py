# I will create create a Python program that analyzes historical stock price data to identify long-term trends and predict 
# future stock movements. Using Pandas and NumPy, the software will clean and process the dataset by filtering, sorting, 
# and aggregating stock prices over time. I will generate key statistics such as moving averages and volatility metrics. 
# To visualize trends, I will use Matplotlib and Seaborn to create time-series graphs. 
# The program will answer two key questions: 
# (1) How has the stock performed over the past years? 
# (2) What patterns or indicators suggest potential future price movements? 
# As a stretch challenge, I will implement an additional visualization to highlight important trends or introduce 
# a third question related to market behavior.

# STRETCH graph to show results
import yfinance as yf
import pandas as pd

# Define the ticker symbol
ticker_symbol = "AAPL"

# Create a Ticker object
ticker = yf.Ticker(ticker_symbol)

# Fetch historical market data
historical_data = ticker.history(period="3y")  # data for the last year
print("Historical Data:")
print(historical_data)

# Fetch basic financials
financials = ticker.financials
print("\nFinancials:")
print(financials)

# Fetch stock actions like dividends and splits
actions = ticker.actions
print("\nStock Actions:")
print(actions)
import yfinance as yf
import pandas as pd

# Download stock data
stock = yf.download("AAPL", start="2020-01-01", end="2025-01-01")

# Save dataset
stock.to_csv("../data/stock_data.csv")

print("Stock data downloaded successfully!")

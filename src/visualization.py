import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../data/processed_stock_data.csv")

# Plot closing price
plt.figure(figsize=(12,6))
plt.plot(df['Close'], label='Closing Price')

# Plot moving averages
plt.plot(df['MA50'], label='50-Day MA')
plt.plot(df['MA100'], label='100-Day MA')

plt.title("Stock Market Analysis")
plt.xlabel("Days")
plt.ylabel("Price")
plt.legend()

# Save image
plt.savefig("../images/trend_analysis.png")

plt.show()

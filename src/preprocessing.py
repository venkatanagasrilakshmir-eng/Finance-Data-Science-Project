import pandas as pd

# Load dataset
df = pd.read_csv("../data/stock_data.csv")

# Remove missing values
df.dropna(inplace=True)

# Convert date column
df['Date'] = pd.to_datetime(df['Date'])

# Create moving averages
df['MA50'] = df['Close'].rolling(window=50).mean()
df['MA100'] = df['Close'].rolling(window=100).mean()

# Save processed data
df.to_csv("../data/processed_stock_data.csv", index=False)

print(df.head())

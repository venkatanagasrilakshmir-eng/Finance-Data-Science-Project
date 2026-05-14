import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import joblib

# Load dataset
df = pd.read_csv("../data/processed_stock_data.csv")

# Remove missing values
df.dropna(inplace=True)

# Features and target
X = df[['Open', 'High', 'Low', 'Volume']]
y = df['Close']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Accuracy
mae = mean_absolute_error(y_test, predictions)
print("Mean Absolute Error:", mae)

# Save model
joblib.dump(model, "../models/stock_model.pkl")

print("Model saved successfully!")

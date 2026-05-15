import os
import pandas as pd
from sklearn.linear_model import LinearRegression


def predict_next_month_expense(file_path):
    if not os.path.exists(file_path):
        print("Expense file not found.")
        return

    df = pd.read_csv(file_path)

    if df.empty:
        print("\nNo expense data available. Please add expenses first.")
        return

    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df = df.dropna(subset=["Date"])

    if df.empty:
        print("No valid date data available.")
        return

    df["Month"] = df["Date"].dt.to_period("M").astype(str)

    monthly_data = df.groupby("Month")["Amount"].sum().reset_index()
    monthly_data = monthly_data.sort_values("Month")

    if len(monthly_data) < 2:
        print("\nPrediction needs expenses from at least 2 different months.")
        print("Example: Add expenses for January and February, then try prediction.")
        return

    monthly_data["Month_Number"] = range(1, len(monthly_data) + 1)

    X = monthly_data[["Month_Number"]]
    y = monthly_data["Amount"]

    model = LinearRegression()
    model.fit(X, y)

    next_month_number = [[len(monthly_data) + 1]]
    predicted_amount = model.predict(next_month_number)[0]

    print("\nMonthly Expense Data Used for Prediction:")
    print(monthly_data[["Month", "Amount"]].to_string(index=False))

    print("\nPrediction Result")
    print("-" * 45)
    print(f"Predicted Spending for Next Month: ₹{predicted_amount:.2f}")

    average_spending = monthly_data["Amount"].mean()

    if predicted_amount > average_spending:
        print("Suggestion: Your spending may increase next month. Try reducing unnecessary expenses.")
    else:
        print("Suggestion: Your spending trend looks controlled.")

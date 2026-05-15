import os
import pandas as pd


def prepare_data(file_path):
    if not os.path.exists(file_path):
        print("Expense file not found.")
        return None

    df = pd.read_csv(file_path)

    if df.empty:
        print("\nNo expense data available. Please add expenses first.")
        return None

    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df = df.dropna(subset=["Date"])
    df["Month"] = df["Date"].dt.to_period("M").astype(str)

    return df


def show_analysis(file_path):
    df = prepare_data(file_path)

    if df is None or df.empty:
        return

    total_expense = df["Amount"].sum()
    average_transaction = df["Amount"].mean()
    highest_expense = df["Amount"].max()
    lowest_expense = df["Amount"].min()
    transaction_count = len(df)

    category_expense = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)
    monthly_expense = df.groupby("Month")["Amount"].sum().sort_index()
    payment_mode_expense = df.groupby("Payment_Mode")["Amount"].sum().sort_values(ascending=False)

    highest_category = category_expense.idxmax()
    highest_category_amount = category_expense.max()

    print("\nComplete Expense Analysis")
    print("-" * 55)
    print(f"Total Expense: ₹{total_expense:.2f}")
    print(f"Average Expense Per Transaction: ₹{average_transaction:.2f}")
    print(f"Highest Single Expense: ₹{highest_expense:.2f}")
    print(f"Lowest Single Expense: ₹{lowest_expense:.2f}")
    print(f"Total Number of Transactions: {transaction_count}")
    print(f"Highest Spending Category: {highest_category} ₹{highest_category_amount:.2f}")

    print("\nCategory-wise Spending:")
    print(category_expense.to_string())

    print("\nMonthly Spending:")
    print(monthly_expense.to_string())

    print("\nPayment Mode-wise Spending:")
    print(payment_mode_expense.to_string())

    print("\nAI-Based Spending Suggestion:")
    if highest_category.lower() == "food":
        print("You spend the most on Food. Try reducing outside food or snacks.")
    elif highest_category.lower() == "shopping":
        print("Shopping is your highest expense. Avoid unnecessary purchases.")
    elif highest_category.lower() == "travel":
        print("Travel expense is high. Try using public transport or student pass.")
    elif highest_category.lower() == "entertainment":
        print("Entertainment expense is high. Set a fixed entertainment budget.")
    elif highest_category.lower() == "education":
        print("Education expense is high, but it can be useful if it supports your learning.")
    else:
        print(f"Your highest spending is in {highest_category}. Try setting a monthly limit for it.")

import os
from datetime import datetime

import pandas as pd


COLUMNS = ["Date", "Category", "Amount", "Payment_Mode", "Description"]


def create_file_if_not_exists(file_path):
    if not os.path.exists(file_path):
        df = pd.DataFrame(columns=COLUMNS)
        df.to_csv(file_path, index=False)


def add_expense(file_path):
    create_file_if_not_exists(file_path)

    print("\nAdd New Expense")
    print("Example categories: Food, Travel, Shopping, Education, Recharge, Entertainment, Other")

    date = input("Enter date (YYYY-MM-DD), or press Enter for today's date: ").strip()

    if date == "":
        date = datetime.today().strftime("%Y-%m-%d")

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    category = input("Enter category: ").strip().title()

    if category == "":
        print("Category cannot be empty.")
        return

    try:
        amount = float(input("Enter amount: ₹"))
        if amount <= 0:
            print("Amount must be greater than 0.")
            return
    except ValueError:
        print("Invalid amount. Please enter numbers only.")
        return

    payment_mode = input("Enter payment mode (Cash/UPI/Card): ").strip().title()

    if payment_mode == "":
        payment_mode = "Not Specified"

    description = input("Enter short description: ").strip()

    if description == "":
        description = "No description"

    new_expense = pd.DataFrame(
        [[date, category, amount, payment_mode, description]],
        columns=COLUMNS
    )

    old_data = pd.read_csv(file_path)
    updated_data = pd.concat([old_data, new_expense], ignore_index=True)
    updated_data.to_csv(file_path, index=False)

    print("Expense added successfully!")


def view_expenses(file_path):
    create_file_if_not_exists(file_path)

    df = pd.read_csv(file_path)

    if df.empty:
        print("\nNo expenses found. Please add expenses first.")
        return

    print("\nAll User-Entered Expenses:")
    print(df.to_string(index=False))


def search_by_category(file_path, category):
    create_file_if_not_exists(file_path)

    df = pd.read_csv(file_path)

    if df.empty:
        print("\nNo expenses found. Please add expenses first.")
        return

    result = df[df["Category"].str.lower() == category.lower()]

    if result.empty:
        print(f"No expenses found for category: {category}")
    else:
        print(f"\nExpenses for category: {category}")
        print(result.to_string(index=False))
        print(f"Total spent on {category}: ₹{result['Amount'].sum():.2f}")


def total_spending(file_path):
    create_file_if_not_exists(file_path)

    df = pd.read_csv(file_path)

    if df.empty:
        print("\nNo expenses found. Please add expenses first.")
        return

    total = df["Amount"].sum()
    print(f"\nTotal Spending from Your Entered Data: ₹{total:.2f}")

import os
import pandas as pd


def budget_warning(file_path, budget):
    if not os.path.exists(file_path):
        print("Expense file not found.")
        return

    if budget <= 0:
        print("Budget must be greater than 0.")
        return

    df = pd.read_csv(file_path)

    if df.empty:
        print("\nNo expense data available. Please add expenses first.")
        return

    total_spent = df["Amount"].sum()
    usage_percentage = (total_spent / budget) * 100

    print("\nBudget Report")
    print("-" * 45)
    print(f"Your Budget: ₹{budget:.2f}")
    print(f"Total Spent: ₹{total_spent:.2f}")
    print(f"Budget Used: {usage_percentage:.2f}%")

    if total_spent > budget:
        print("Warning: You have crossed your budget!")
    elif usage_percentage >= 80:
        print("Alert: You have used more than 80% of your budget.")
    else:
        print("Good! You are spending within your budget.")

import os
import pandas as pd
import matplotlib.pyplot as plt


def load_data(file_path):
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


def category_bar_graph(df):
    category_expense = df.groupby("Category")["Amount"].sum()

    plt.figure(figsize=(8, 5))
    category_expense.plot(kind="bar")
    plt.title("Category-wise Spending")
    plt.xlabel("Category")
    plt.ylabel("Amount Spent")
    plt.tight_layout()
    plt.savefig("outputs/category_bar_graph.png")
    plt.show()


def category_pie_chart(df):
    category_expense = df.groupby("Category")["Amount"].sum()

    plt.figure(figsize=(7, 7))
    category_expense.plot(kind="pie", autopct="%1.1f%%")
    plt.title("Category-wise Spending Percentage")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig("outputs/category_pie_chart.png")
    plt.show()


def monthly_line_graph(df):
    monthly_expense = df.groupby("Month")["Amount"].sum()

    plt.figure(figsize=(8, 5))
    monthly_expense.plot(kind="line", marker="o")
    plt.title("Monthly Spending Trend")
    plt.xlabel("Month")
    plt.ylabel("Amount Spent")
    plt.tight_layout()
    plt.savefig("outputs/monthly_line_graph.png")
    plt.show()


def generate_all_graphs(file_path):
    df = load_data(file_path)

    if df is None or df.empty:
        return

    category_bar_graph(df)
    category_pie_chart(df)

    if df["Month"].nunique() >= 2:
        monthly_line_graph(df)
    else:
        print("Monthly line graph needs expenses from at least 2 different months.")

    print("\nGraphs generated and saved in the outputs folder.")

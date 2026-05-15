import os

from tracker import add_expense, view_expenses, search_by_category, total_spending
from analysis import show_analysis
from graphs import generate_all_graphs
from prediction import predict_next_month_expense
from budget import budget_warning


DATA_FILE = "data/expenses.csv"


def show_menu():
    print("\n" + "=" * 55)
    print("       AI PERSONAL FINANCE TRACKER")
    print("=" * 55)
    print("1. Add New Expense")
    print("2. View All Expenses")
    print("3. Search Expenses by Category")
    print("4. Show Total Spending")
    print("5. Show Complete Expense Analysis")
    print("6. Generate Spending Graphs")
    print("7. Budget Warning")
    print("8. Predict Next Month Spending")
    print("9. Exit")


def main():
    os.makedirs("data", exist_ok=True)
    os.makedirs("outputs", exist_ok=True)

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense(DATA_FILE)

        elif choice == "2":
            view_expenses(DATA_FILE)

        elif choice == "3":
            category = input("Enter category name: ").strip()
            search_by_category(DATA_FILE, category)

        elif choice == "4":
            total_spending(DATA_FILE)

        elif choice == "5":
            show_analysis(DATA_FILE)

        elif choice == "6":
            generate_all_graphs(DATA_FILE)

        elif choice == "7":
            try:
                budget = float(input("Enter your monthly budget: ₹"))
                budget_warning(DATA_FILE, budget)
            except ValueError:
                print("Invalid input. Please enter budget in numbers only.")

        elif choice == "8":
            predict_next_month_expense(DATA_FILE)

        elif choice == "9":
            print("Thank you for using AI Personal Finance Tracker.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

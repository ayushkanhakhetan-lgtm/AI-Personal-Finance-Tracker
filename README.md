# AI Personal Finance Tracker - User Input Based Project

## Important Note
This version does not use pre-filled expense data.
The CSV file is empty at the beginning.
All analysis, graphs, budget warning, and prediction are based only on the expenses entered by the user.

## Problem Statement
Students often spend money on food, travel, shopping, recharge, and entertainment without tracking expenses. This project helps students record their own expenses and analyze spending habits.

## Objective
To create a Python-based AI Personal Finance Tracker that takes user input, stores expenses, analyzes spending patterns, shows graphs, gives budget warnings, and predicts future spending.

## Features
1. Add expense from user input
2. View all user-entered expenses
3. Search expenses by category
4. Show total spending
5. Analyze spending by category, month, and payment mode
6. Generate graphs
7. Show budget warning
8. Predict next month spending using Linear Regression
9. Give saving suggestions

## Tech Stack
- Python
- Pandas
- Matplotlib
- Scikit-learn
- CSV File Storage

## How to Run

### Step 1: Install libraries
```bash
pip install -r requirements.txt
```

### Step 2: Run project
```bash
python main.py
```

If Python command does not work on Windows, use:

```bash
py main.py
```

## How to Use
1. First select option 1 and add multiple expenses.
2. Add expenses from different dates and categories.
3. Then use analysis and graph options.
4. For prediction, add expenses from at least 2 different months.

## AIML Concepts Used
- Data Analysis
- Linear Regression
- Forecasting
- Pattern Identification
- Budget Recommendation

## Future Scope
- Login system
- Web dashboard
- Mobile app
- Database storage
- Automatic UPI/SMS expense reading
- Personalized AI saving advisor

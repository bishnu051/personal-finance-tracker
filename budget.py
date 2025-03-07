import pandas as pd
from data import load_data
import os

budget_file = "budget.csv"

def set_monthly_income():
    """Set and save the monthly income to the budget file."""
    while True:
        income_input = input("Enter your total monthly income (* to Cancel): ")
        if income_input == "*":
            print("Monthly income entry canceled.")
            return
        try:
            income = float(income_input)
            if income > 0:
                break
            print("Income must be a positive value!")
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

    budget_data = pd.DataFrame({"Type": ["Monthly Income"], "Amount": [income]})
    budget_data.to_csv(budget_file, index=False)
    print(f"Monthly income of ${income:.2f} saved successfully!")

def set_category_budget():
    """Set and save the budgets for different spending categories."""
    categories = ["Food", "Rent", "Utilities", "Transport", "Other"]

    # Load existing budget file if it exists
    if os.path.exists(budget_file):
        budget_data = pd.read_csv(budget_file)
    else:
        budget_data = pd.DataFrame(columns=["Type", "Amount"])

    print("\n--- Set Category Budgets (Enter * to Cancel) ---")
    budget_list = []
    for category in categories:
        while True:
            budget_input = input(f"Enter budget for {category} (* to Cancel): ")
            if budget_input == "*":
                print("Budget entry canceled.")
                return
            try:
                budget = float(budget_input)
                if budget >= 0:
                    break
                print("Budget cannot be negative!")
            except ValueError:
                print("Invalid input! Please enter a numeric value.")

        budget_list.append({"Type": category, "Amount": budget})

    # Add category budgets to the dataframe
    new_budget_data = pd.DataFrame(budget_list)
    budget_data = pd.concat([budget_data, new_budget_data], ignore_index=True)

    # Save updated budget data
    budget_data.to_csv(budget_file, index=False)
    print("\nCategory budgets saved successfully!")

def load_budget():
    """Load budget data from the budget file."""
    if not os.path.exists(budget_file):
        return {}

    budget_data = pd.read_csv(budget_file)
    return dict(zip(budget_data["Type"], budget_data["Amount"]))

def check_budget_status():
    """Compare spending against the budget and show warnings/suggestions for the latest month."""
    data = load_data("sampledata.csv")  # Load transaction data
    budgets = load_budget()

    if not budgets:
        print("\nNo budget data found! Please set your budget first.")
        return

    if data.empty:
        print("\nNo transactions found!")
        return

    # Convert Date column to datetime format
    data["Date"] = pd.to_datetime(data["Date"])

    # Find the most recent month in the dataset
    latest_month = data["Date"].dt.to_period("M").max()

    # Filter data for the latest month only
    latest_month_data = data[data["Date"].dt.to_period("M") == latest_month]

    if latest_month_data.empty:
        print(f"\nNo transactions found for the latest month: {latest_month}")
        return

    # Group total expenses by category for the latest month
    spending = latest_month_data[latest_month_data["Type"] == "Expense"].groupby("Category")["Amount"].sum()

    print(f"\n--- Budget Status for {latest_month} ---")
    for category, budget in budgets.items():
        if category == "Monthly Income":
            continue  # Skip income since it's not an expense

        spent = spending.get(category, 0)
        status = ""

        if spent > budget:
            status = "(Alert: Exceeded budget!)"
        elif spent >= 0.9 * budget:
            status = "(Warning: Close to budget!)"

        print(f"- {category}: ${spent:.2f} / ${budget:.2f} {status}")

        # Suggestions
        if spent > budget:
            print(f"  Suggestion: Consider reducing {category} spending.")


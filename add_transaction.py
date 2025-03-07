import pandas as pd
import datetime
from data import load_data, save_data

# categories for selection
categories = {
    1: "Food",
    2: "Rent",
    3: "Utilities",
    4: "Transport",
    5: "Income",
    6: "Investment",
    7: "Other"
}

def validate_date(input_date):
    """Validate the date format (YYYY-MM-DD)."""
    try:
        datetime.datetime.strptime(input_date, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def add_transaction():
    """Add a new transaction with an option to cancel at any point using '*'."""
    data = load_data("sampledata.csv")
    print("\n--- Add a New Transaction (Enter * to Cancel) ---")

    # Validate date input
    while True:
        date = input("Enter date (YYYY-MM-DD): ")
        if date == "*":
            print("Transaction entry canceled.")
            return
        if validate_date(date):
            break
        print("Invalid date format! Please enter in YYYY-MM-DD format.")

    # Display category options
    print("\nSelect a category (Enter * to Cancel):")
    for num, cat in categories.items():
        print(f"{num}. {cat}")

    # Validate category input
    while True:
        try:
            category_num = input("Enter category number: ")
            if category_num == "*":
                print("Transaction entry canceled.")
                return
            category_num = int(category_num)
            if category_num in categories:
                category = categories[category_num]
                break
            else:
                print("Invalid category number! Please choose a valid number.")
        except ValueError:
            print("Invalid input! Please enter a number.")

    description = input("Enter description (or * to Cancel): ")
    if description == "*":
        print("Transaction entry canceled.")
        return

    # Validate amount input
    while True:
        try:
            amount = input("Enter amount (or * to Cancel): ")
            if amount == "*":
                print("Transaction entry canceled.")
                return
            amount = float(amount)
            if amount > 0:
                break
            print("Amount must be positive!")
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

    # determine transaction type
    transaction_type = "Income" if category == "Income" else "Expense"

    # new transaction as a DataFrame row
    new_transaction = pd.DataFrame([[date, category, description, amount, transaction_type]],
                                   columns=["Date", "Category", "Description", "Amount", "Type"])

    # Appending new transaction to existing data
    data = pd.concat([data, new_transaction], ignore_index=True)

    # Saving updated data
    save_data(data, "sampledata.csv")

    print("\nTransaction added successfully!")

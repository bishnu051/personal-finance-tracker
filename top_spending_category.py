from data import load_data
import pandas as pd

def top_spending_category():
    """Finds the top spending category and displays total spend with monthly breakdown."""
    data = load_data()

    if data.empty:
        print("\nNo transactions found! Cannot analyze spending.")
        return None

    # Convert 'Date' column to datetime format
    data['Date'] = pd.to_datetime(data['Date'], errors="coerce")

    # Filter only expenses
    expense_data = data[data['Type'] == 'Expense']

    if expense_data.empty:
        print("\nNo expenses found in the data.")
        return None

    # Group by category and sum the expenses
    spending_by_category = expense_data.groupby('Category')['Amount'].sum()

    # Identify the top spending category
    top_category = spending_by_category.idxmax()
    top_category_total = spending_by_category.max()

    print(f"Top Spending Category: {top_category} - ${top_category_total:.2f}")

    # Monthly breakdown for the top category
    monthly_spending = expense_data[expense_data['Category'] == top_category] \
        .groupby(expense_data['Date'].dt.to_period("M"))['Amount'].sum()

    print("--- Monthly Spending Breakdown ---")
    print(monthly_spending.to_string(index=True))  # Show in a clean format

    return top_category, monthly_spending
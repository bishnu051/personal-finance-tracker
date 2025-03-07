from data import load_data, save_data
import matplotlib.pyplot as plt
import pandas as pd


def analyze_spending():
    """Pie chart representation of expenses for the latest month with highest expenses highlighted."""
    data = load_data()

    if data.empty:
        print("\nNo transactions found! Cannot analyze spending.")
        return

    # Convert Date column to datetime format
    data["Date"] = pd.to_datetime(data["Date"], errors="coerce")

    # Find the most recent month in the dataset
    latest_month = data["Date"].dt.to_period("M").max()

    # Filter data for the latest month only
    latest_month_data = data[data["Date"].dt.to_period("M") == latest_month]

    if latest_month_data.empty:
        print(f"\nNo transactions found for the latest month: {latest_month}")
        return

    # Calculate total expenses per category for the latest month
    spending = latest_month_data[latest_month_data['Type'] == 'Expense'].groupby('Category')['Amount'].sum()

    if spending.empty:
        print(f"\nNo expenses recorded for {latest_month}.")
        return

    print(f"\n--- Spending by Category for {latest_month} ---")
    print(spending)

    # Highlight the category with the highest spending by separation
    explode = [0.1 if amount == spending.max() else 0 for amount in spending]

    plt.figure(figsize=(8, 8))
    plt.pie(spending, labels=spending.index, autopct='%1.1f%%',
            explode=explode, wedgeprops={'edgecolor': 'black'})

    plt.title(f'Spending by Category - {latest_month}', fontsize=14, fontweight='bold')
    plt.tight_layout()  # Prevents text cutoff
    plt.show()


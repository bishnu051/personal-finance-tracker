from data import load_data
import pandas as pd

def average_monthly_spending():
    data = load_data()
    data['Date'] = pd.to_datetime(data['Date'])
    data['Month'] = data['Date'].dt.to_period('M')
    monthly_total = data[data['Type'] == 'Expense'].groupby('Month')['Amount'].sum()
    avg_total_spending = monthly_total.mean()

    avg_spending_by_category = data[data['Type'] == 'Expense'].groupby(['Month', 'Category'])['Amount'].sum().groupby(
        'Category').mean()

    print("--- Average Monthly Spending (Total) ---")
    print(f"Average Monthly Spending: ${avg_total_spending:.2f}")

    print("--- Average Monthly Spending by Category ---")
    print(avg_spending_by_category)

    return avg_total_spending, avg_spending_by_category



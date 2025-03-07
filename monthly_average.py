import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sampledata.csv")
df['Date'] = pd.to_datetime(df['Date'])

def average_monthly_spending():
    df['Month'] = df['Date'].dt.to_period('M')
    monthly_total = df[df['Type'] == 'Expense'].groupby('Month')['Amount'].sum()
    avg_total_spending = monthly_total.mean()

    avg_spending_by_category = df[df['Type'] == 'Expense'].groupby(['Month', 'Category'])['Amount'].sum().groupby(
        'Category').mean()

    print("--- Average Monthly Spending (Total) ---")
    print(f"Average Monthly Spending: ${avg_total_spending:.2f}")

    print("--- Average Monthly Spending by Category ---")
    print(avg_spending_by_category)

    return avg_total_spending, avg_spending_by_category


average_monthly_spending()
from data import load_data
import pandas as pd

def top_spending_category():
    data = load_data()
    data['Date'] = pd.to_datetime(data['Date'])
    spending_by_category = data[data['Type'] == 'Expense'].groupby('Category')['Amount'].sum()
    top_category = spending_by_category.idxmax()
    top_category_total = spending_by_category.max()

    print(f"Top Spending Category: {top_category} - ${top_category_total:.2f}")

    return top_category


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sampledata.csv")
df['Date'] = pd.to_datetime(df['Date'])

def top_spending_category():
    spending_by_category = df[df['Type'] == 'Expense'].groupby('Category')['Amount'].sum()
    top_category = spending_by_category.idxmax()
    top_category_total = spending_by_category.max()

    print(f"Top Spending Category: {top_category} - ${top_category_total:.2f}")

    return top_category

top_spending_category()
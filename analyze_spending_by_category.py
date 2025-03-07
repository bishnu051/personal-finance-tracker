import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sampledata.csv")
# Analyze Spending by Category
def analyze_spending():
    spending = df[df['Type'] == 'Expense'].groupby('Category')['Amount'].sum()
    print("--- Spending by Category ---")
    print(spending)
    spending.plot(kind='bar', title='Spending by Category')
    plt.xlabel('Category')
    plt.ylabel('Total Amount')
    plt.show()

analyze_spending()
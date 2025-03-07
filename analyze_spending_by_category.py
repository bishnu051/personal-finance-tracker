from data import load_data, save_data
import matplotlib.pyplot as plt

# Analyze Spending by Category
def analyze_spending():
    data = load_data()
    spending = data[data['Type'] == 'Expense'].groupby('Category')['Amount'].sum()
    print("--- Spending by Category ---")
    print(spending)
    spending.plot(kind='bar', figsize=(10, 6), title='Spending by Category')
    plt.xlabel('Category')
    plt.ylabel('Total Amount')
    plt.show()


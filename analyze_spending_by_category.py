from data import load_data, save_data
import matplotlib.pyplot as plt

# pie chart representation of expenses with highest expenses highlighted by separation
def analyze_spending():
    data = load_data()
    spending = data[data['Type'] == 'Expense'].groupby('Category')['Amount'].sum()

    print("\n--- Spending by Category ---")
    print(spending)

    # Highlight the category with the highest spending
    max = [0.1 if amount == spending.max() else 0 for amount in spending]

    # Create the improved pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(spending, labels=spending.index, autopct='%1.1f%%', startangle=140,
             explode=max, wedgeprops={'edgecolor': 'black'})

    plt.title('Spending by Category', fontsize=14, fontweight='bold')
    plt.show()

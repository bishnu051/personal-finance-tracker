#data visualiazation for personal finance app tracker
import matplotlib.pyplot as plt
import pandas as pd
from data import load_data
from budget import load_budget
def plot_income_vs_expense():
    data = load_data()
    """Visualizes income vs. expenses over time."""
    # Convert 'Date' column to datetime format
    data['Date'] = pd.to_datetime(data['Date'])
    # Sort transactions by date for proper trend visualization
    df_sorted = data.sort_values('Date')

    # Group transactions by month and type (Income/Expense) and sum up amounts
    monthly_data = df_sorted.groupby([df_sorted['Date'].dt.to_period('M'), 'Type'])['Amount'].sum().unstack().fillna(0)

    # Create a line chart for income vs. expenses over time
    plt.figure(figsize=(10, 5))
    plt.plot(monthly_data.index.astype(str), monthly_data.get('Income', 0), marker='o', linestyle='-', label='Income',
             color='green')
    plt.plot(monthly_data.index.astype(str), monthly_data.get('Expense', 0), marker='o', linestyle='-',
             label='Expenses', color='red')

    plt.title('Monthly Income vs. Expenses')
    plt.xlabel('Month')
    plt.ylabel('Amount ($)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()


def plot_spending_vs_budget():
    data = load_data()
    budget_dict = load_budget()
    """Visualizes spending by category vs. set budget with alerts."""
    # Calculate total spending for each category
    category_totals = data[data['Type'] == 'Expense'].groupby('Category')['Amount'].sum()
    categories = category_totals.index.tolist()
    spending = category_totals.values.tolist()

    # Retrieve budget amounts for each category, defaulting to 0 if not provided
    budget = [budget_dict.get(cat, 0) for cat in categories]

    # Set color: Red if spending exceeds budget, Green if within budget
    colors = ['red' if spend > bud else 'green' for spend, bud in zip(spending, budget)]

    # Create a bar chart to compare actual spending vs. budget
    plt.figure(figsize=(8, 5))
    bar_width = 0.4
    index = range(len(categories))

    plt.bar(index, spending, width=bar_width, label='Actual Spending', color=colors)
    plt.bar([i + bar_width for i in index], budget, width=bar_width, label='Budget', color='blue', alpha=0.7)

    plt.xlabel('Category')
    plt.ylabel('Amount ($)')
    plt.title('Spending vs. Budget by Category')
    plt.xticks([i + bar_width / 2 for i in index], categories, rotation=45)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()


def plot_expense_distribution():
    data = load_data()
    """Displays a pie chart of expense distribution across categories."""
    # Calculate total spending per category
    category_totals = data[data['Type'] == 'Expense'].groupby('Category')['Amount'].sum()

    # Create a pie chart to show the percentage of each category's spending
    plt.figure(figsize=(8, 8))
    plt.pie(category_totals, labels=category_totals.index, autopct='%1.1f%%', startangle=140,
            colors=plt.cm.Paired.colors)
    plt.title('Expense Distribution by Category')
    plt.tight_layout()
    plt.show()

def visualization_menu():
    """Displays the visualization menu and handles user choice."""
    while True:
        print("\nChoose a visualization:")
        print("1. Spending vs. Budget")
        print("2. Income vs. Expense")
        print("3. Expense Distribution")
        print("* to Cancel")

        choice = input("Enter the number for the visualization: ").strip()

        if choice == "*":
            print("Exiting visualization menu...")
            break

        try:
            choice = int(choice)
            if choice == 1:
                plot_spending_vs_budget()
            elif choice == 2:
                plot_income_vs_expense()
            elif choice == 3:
                plot_expense_distribution()
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number (1-3) or '*' to cancel.")


#data visualiazation for personal finance app tracker
import matplotlib.pyplot as plt
import pandas as pd
def plot_income_vs_expense(df):
    """Visualizes income vs. expenses over time."""
    # Convert 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'])
    # Sort transactions by date for proper trend visualization
    df_sorted = df.sort_values('Date')

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


def plot_spending_vs_budget(df, budget_dict):
    """Visualizes spending by category vs. set budget with alerts."""
    # Calculate total spending for each category
    category_totals = df[df['Type'] == 'Expense'].groupby('Category')['Amount'].sum()
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


def plot_expense_distribution(df):
    """Displays a pie chart of expense distribution across categories."""
    # Calculate total spending per category
    category_totals = df[df['Type'] == 'Expense'].groupby('Category')['Amount'].sum()

    # Create a pie chart to show the percentage of each category's spending
    plt.figure(figsize=(8, 8))
    plt.pie(category_totals, labels=category_totals.index, autopct='%1.1f%%', startangle=140,
            colors=plt.cm.Paired.colors)
    plt.title('Expense Distribution by Category')
    plt.tight_layout()
    plt.show()


# Example Usage:
if __name__ == "__main__":
    # Sample dataset containing transactions
    data = {
        'Date': ['2024-10-01', '2024-10-02', '2024-10-02', '2024-10-03', '2024-10-04', '2024-10-06'],
        'Category': ['Food', 'Rent', 'Utilities', 'Food', 'Transport', 'Income'],
        'Description': ['Grocery', 'Monthly Rent', 'Electricity Bill', 'Dinner', 'Bus Ticket', 'Salary'],
        'Amount': [50.75, 1200.00, 60.00, 30.00, 2.75, 2000.00],
        'Type': ['Expense', 'Expense', 'Expense', 'Expense', 'Expense', 'Income']
    }
    df_sample = pd.DataFrame(data)

    # Example budget dictionary defining spending limits per category
    budget_example = {'Food': 500, 'Rent': 1200, 'Utilities': 200, 'Transport': 150}

    # Generate visualizations
    plot_income_vs_expense(df_sample)
    plot_spending_vs_budget(df_sample, budget_example)
    plot_expense_distribution(df_sample)

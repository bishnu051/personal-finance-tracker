from category_budget import set_category_budget
import pandas as pd

df = pd.read_csv("sampledata.csv")
df['Date'] = pd.to_datetime(df['Date'])
budgets = set_category_budget()

def check_budget_status():
    spending = df[df['Type'] == 'Expense'].groupby('Category')['Amount'].sum()
    print("\n--- Budget Status ---")
    for category, budget in budgets.items():
        spent = spending.get(category, 0)
        status = ""
        if spent > budget:
            status = "(Alert: Exceeded budget!)"
        elif spent >= 0.9 * budget:
            status = "(Warning: Close to budget!)"
        print(f"- {category}: ${spent:.2f} / ${budget:.2f} {status}")

        if spent > budget:
            print(f"  Suggestion: Consider reducing {category} spending.")

check_budget_status()
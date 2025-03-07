def set_category_budget():
    budgets = {}
    categories = ['Food', 'Rent', 'Utilities', 'Transport']
    for category in categories:
        while True:
            try:
                budget = float(input(f"Enter your budget for {category}: "))
                if budget < 0:
                    raise ValueError("Budget cannot be negative. Please enter a valid amount.")
                budgets[category] = budget
                break
            except ValueError as e:
                print(f"Invalid input: Please enter amount")
    print("Your budgets have been set:")
    for category, amount in budgets.items():
        print(f"- {category}: ${amount:.2f}")
    return budgets

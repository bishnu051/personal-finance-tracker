def set_monthly_income():
    income = float(input("Enter your total monthly income: "))
    print(f"Your monthly income is set to: ${income:.2f}")
    return income

set_monthly_income()

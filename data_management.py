

def add_transaction():
    def time_date():
        from datetime import datetime
        try:
            t_date_str = input("Please enter the expense day (YYYY-MM-DD): ")
            expense_date = datetime.strptime(t_date_str, "%Y-%m-%d")
            print(expense_date)
            return expense_date

        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    def description_expense():
        description = input("Enter description of your expense:  ")
        if description == "":
            print("Please enter a valid character.")
        # Check the first character of the task. It must be a letter!
        elif not description[0].isalpha():
            print("Please enter a valid task. Must start with a letter")
        elif len(description) > 200:
            print("Please enter a valid task. 200 characters maximum")
        else:
            return description

    def amount_expense():
        while True:
            try:
                amount = float(input("Enter the amount of expense:    $"))
                if amount == "":
                    print("Please enter a valid character.")
                break
            except ValueError:
                print("Please enter a valid character (number)")
        return amount

    def category_expense():
        expense_categories = [
            "Food",
            "Home",
            "Work",
            "Fun",
            "Fitness",
            "Miscellaneous",
        ]

        while True:
            print("Select a category:  ")
            for i, category_name in enumerate(expense_categories):
                print(f"{i + 1}. {category_name}")

            while True:
                try:
                    value_range = f"[1 - {len(expense_categories)}]"
                    selected_index = int(input(f"Enter a category number: {value_range}:  ")) - 1

                    if selected_index == "":
                        print("Please enter a valid character.")
                    break
                except ValueError:
                    print("Please enter a valid character (number)")
            if selected_index in range(len(expense_categories)):
                selected_category = expense_categories[selected_index]
                return selected_category
            else:
                print("Invalid category. Please try again")

    def type_expense():
        while True:
            try:
                ingreso = str(input("Select the type (expense or income):  "))
                ing = ingreso.upper()
                if ing == "EXPENSE":
                    print("Expense was added")
                    return ing
                elif ing == "INCOME":
                    print("Income was added")
                    return ing
            except ValueError:
                print("Please enter a valid type (expense or income)")
    import pandas as pd
    date=time_date()
    category=category_expense()
    description= description_expense()
    amount= amount_expense()
    type_enter= type_expense()

    expense_add= {"Date": date, "Category":category, "Description": description, "Amount":amount, "Type":type_enter}

    df=pd.read_csv("finance_tracker.csv")
    df.loc[len(df)]=expense_add
    df.drop(['Unnamed: 0'], axis=1, inplace=True)

    df.to_csv("finance_tracker.csv")
    print(f"Your transaction was added {df}")

def delete_transaction():
    import pandas as pd
    finance_tracker= pd.read_csv("finance_tracker.csv")
    df=pd.DataFrame(finance_tracker)
    df.drop(['Unnamed: 0'], axis=1, inplace=True)
    print(df)
    delete_row=int(input("Select the index do you wanna delete:   "))

    #df.drop(['Index'], axis=1, inplace=True)
    df.drop(index=[delete_row], axis= 0, inplace=True)
    df.to_csv("finance_tracker.csv")

    print("Your transaction was deleted")
    print(df)

def edit_transaction():
    import pandas as pd
    finance_tracker = pd.read_csv("finance_tracker.csv")
    df = pd.DataFrame(finance_tracker)
    df.drop(['Unnamed: 0'], axis=1, inplace=True)
    print(df)
    edith_row = int(input("Select the index do you want to edith:   "))

    def time_date():
        from datetime import datetime
        try:
            t_date_str = input("Please enter the expense day (YYYY-MM-DD): ")
            expense_date = datetime.strptime(t_date_str, "%Y-%m-%d")
            print(expense_date)
            return expense_date

        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    def description_expense():
        description = input("Enter description of your expense:  ")
        if description == "":
            print("Please enter a valid character.")
        # Check the first character of the task. It must be a letter!
        elif not description[0].isalpha():
            print("Please enter a valid task. Must start with a letter")
        elif len(description) > 200:
            print("Please enter a valid task. 200 characters maximum")
        else:
            return description

    def amount_expense():
        while True:
            try:
                amount = float(input("Enter the amount of expense:    $"))
                if amount == "":
                    print("Please enter a valid character.")
                break
            except ValueError:
                print("Please enter a valid character (number)")
        return amount

    def category_expense():
        expense_categories = [
            "Food",
            "Home",
            "Work",
            "Fun",
            "Fitness",
            "Miscellaneous",
        ]

        while True:
            print("Select a category:  ")
            for i, category_name in enumerate(expense_categories):
                print(f"{i + 1}. {category_name}")

            while True:
                try:
                    value_range = f"[1 - {len(expense_categories)}]"
                    selected_index = int(input(f"Enter a category number: {value_range}:  ")) - 1

                    if selected_index == "":
                        print("Please enter a valid character.")
                    break
                except ValueError:
                    print("Please enter a valid character (number)")
            if selected_index in range(len(expense_categories)):
                selected_category = expense_categories[selected_index]
                return selected_category
            else:
                print("Invalid category. Please try again")

    def type_expense():
        while True:
            try:
                ingreso = str(input("Select the type (expense or income):  "))
                ing = ingreso.upper()
                if ing == "EXPENSE":
                    print("Expense was added")
                    return ing
                elif ing == "INCOME":
                    print("Income was added")
                    return ing
            except ValueError:
                print("Please enter a valid type (expense or income)")

    import pandas as pd
    date = time_date()
    category = category_expense()
    description = description_expense()
    amount = amount_expense()
    type_enter = type_expense()

    expense_add = {"Date": date, "Category": category, "Description": description, "Amount": amount, "Type": type_enter}


    df.loc[edith_row,:] = expense_add
    df.to_csv("finance_tracker.csv")
    print(f"Your transaction was added {df}")

def view_range():
    import pandas as pd
    finance_tracker = pd.read_csv("finance_tracker.csv")
    df = pd.DataFrame(finance_tracker)
    df.sort_values(by="Date", ascending= False)
    df.drop(['Unnamed: 0'], axis=1, inplace=True)

    print(df)
    print("Please enter the date range you wish to obtain information about ")

    from datetime import datetime
    try:
        date1 = input("Please enter the expense day (YYYY-MM-DD): ")
        date2 = input("Please enter the expense day (YYYY-MM-DD): ")

        #filter data between tow dates
        expense_date = datetime.strptime(date1, "%Y-%m-%d")
        expense_date2 = datetime.strptime(date2, "%Y-%m-%d")

        if expense_date>expense_date2:

            filtered_df = df.loc[(df['Date'] >= date2)
                                 & (df['Date'] <= date1)]
            print(filtered_df)

        else:

            filtered_df = df.loc[(df['Date'] >= date1)
                                 & (df['Date'] <= date2)]
            print(filtered_df)

    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

def view_all():
    import pandas as pd
    finance_tracker = pd.read_csv("finance_tracker.csv")
    df = pd.DataFrame(finance_tracker)
    df.sort_values(by="Date", ascending= False)
    df.drop(['Unnamed: 0'], axis=1, inplace=True)

    print(df)

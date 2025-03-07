import pandas as pd
from data import load_data, save_data

def edit_transaction(index):
    """Edit specific fields of an existing transaction by its index, with option to cancel using '*'."""
    data = load_data()

    if index < 0 or index >= len(data):
        print("Error: Invalid transaction index!")
        return

    print("\n--- Current Transaction Details ---")
    print(data.iloc[index])

    while True:
        print("\nWhich field do you want to edit?")
        print("1. Date")
        print("2. Category")
        print("3. Description")
        print("4. Amount")
        print("5. Type (Income/Expense)")
        print("6. Finish Editing")

        choice = input("Enter the number of the field to edit (* to cancel): ")
        if choice == "*":
            print("Transaction editing canceled.")
            return

        if choice == "1":
            new_date = input(f"Enter new date (YYYY-MM-DD) [{data.at[index, 'Date']}]: ")
            if new_date == "*":
                print("Transaction editing canceled.")
                return
            if new_date:
                data.at[index, 'Date'] = new_date
        elif choice == "2":
            new_category = input(f"Enter new category [{data.at[index, 'Category']}]: ")
            if new_category == "*":
                print("Transaction editing canceled.")
                return
            if new_category:
                data.at[index, 'Category'] = new_category
        elif choice == "3":
            new_description = input(f"Enter new description [{data.at[index, 'Description']}]: ")
            if new_description == "*":
                print("Transaction editing canceled.")
                return
            if new_description:
                data.at[index, 'Description'] = new_description
        elif choice == "4":
            new_amount = input(f"Enter new amount [{data.at[index, 'Amount']}]: ")
            if new_amount == "*":
                print("Transaction editing canceled.")
                return
            if new_amount:
                try:
                    data.at[index, 'Amount'] = float(new_amount)
                except ValueError:
                    print("Invalid amount! Please enter a numeric value.")
        elif choice == "5":
            new_type = input(f"Enter new type (Income/Expense) [{data.at[index, 'Type']}]: ")
            if new_type == "*":
                print("Transaction editing canceled.")
                return
            if new_type in ["Income", "Expense"]:
                data.at[index, 'Type'] = new_type
            else:
                print("Invalid type! Please enter 'Income' or 'Expense'.")
        elif choice == "6":
            break
        else:
            print("Invalid choice! Please enter a number from 1 to 6 or '*' to cancel.")

    # Save updated data
    save_data(data)
    print("\nTransaction updated successfully!")

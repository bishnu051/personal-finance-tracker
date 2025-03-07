#The stable production branch containing the latest release-ready code.
from delete_transaction import delete_transaction
from edit_transaction import edit_transaction
from add_transaction import add_transaction
from transaction_by_date_range import view_transactions_by_date
from data import load_data, save_data, view_data, export_data
from analyze_spending_by_category import analyze_spending
from monthly_average import average_monthly_spending
from top_spending_category import top_spending_category
from budget import set_monthly_income, set_category_budget, check_budget_status
from visualization import visualization_menu

if __name__ == "__main__":
    print("\n")
    print ("HELLO THIS IS YOUR FINANCE TRACKER")
    print("\n")

    while True:
        print("\n=== Personal Finance Tracker ===")
        print("1. View All Transactions")
        print("2. View Transactions by Date Range")
        print("3. Add a Transaction")
        print("4. Edit a Transaction")
        print("5. Delete a Transaction")
        print("6. Analyze Spending by Category")
        print("7. Calculate Average Monthly Spending")
        print("8. Show Top Spending Category")
        print("9. Set Monthly Income")
        print("10. Set Category Budget")
        print("11. Check Budget Status")
        print("12. Visualize Spending Trends")
        print("13. Save Transactions to CSV")
        print("14. Exit")

        user_choice = input("Choose an option (1-14): ")
        print("\n")

        if user_choice == "1":
            view_data()
        elif user_choice == "2":
            view_transactions_by_date()
        elif user_choice == "3":
            add_transaction()
        elif user_choice == "4":
            view_data()
            index = int(input("Enter transaction index to edit: "))
            edit_transaction(index)
        elif user_choice == "5":
            delete_transaction()
        elif user_choice == "6":
            analyze_spending()
        elif user_choice == "7":
            average_monthly_spending()
        elif user_choice == "8":
            top_spending_category()
        elif user_choice == "9":
            set_monthly_income()
        elif user_choice == "10":
            set_category_budget()
        elif user_choice == "11":
            check_budget_status()
        elif user_choice == "12":
           visualization_menu()
        elif user_choice == "13":
           export_data()
        elif user_choice == "14":
            print("Goodbye!")
            break
        else:
            print("Sorry, please enter a valid option")

#The stable production branch containing the latest release-ready code.

if __name__ == "__main__":
    print("\n")
    print ("HELLO THIS IS YOUR FINANCE TRACKER")
    print("\n")

    while True:
        print("")
        print("what do you wanna do today?")
        print("Please select one of the following option")
        print("\n")
        print("(1) View All Transactions")
        print("(2) View Transactions by Date Range")
        print("(3) Add a Transaction")
        print("(4) Edit a Transaction")
        print("(5) Delete a Transaction")
        print("(6) Analyze Spending by Category")
        print("(7) Calculate Average Monthly Spending")
        print("(8) Show Top Spending Category")
        print("(9) Visualize Monthly Spending Trend")
        print("(10) Exit")

        choise = input ("Enter your choise: ")
        print("\n")

        if (choise == "1"):
            view_transactions()
        elif (choise == "2"):
            view_transactions()
        elif (choise == "3"):
            add_transaction ()
        elif (choise == "4"):
            edit_transaction()
        elif (choise == "5"):
            delete_transaction()
        elif (choise == "6"):
            analyze_spending()
        elif (choise == "7"):
            monyhly_spending()
        elif (choise == "8"):
            top_spending()
        elif (choise == "9"):
            spending_trend()
        elif (choise == "11"):

            break
        else:
            print("Sorry, please enter a valid option")
    print("Goodbye")

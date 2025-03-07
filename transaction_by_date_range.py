import pandas as pd
from data import load_data

def view_transactions_by_date():
    """View transactions within a specific date range."""
    data = load_data("new.csv")  # Load the latest transactions

    if data.empty:
        print("\nNo transactions found!")
        return

    print("\n--- View Transactions by Date Range ---")

    # Get valid start date
    while True:
        start_date = input("Enter start date (YYYY-MM-DD): ")
        try:
            pd.to_datetime(start_date)  # Validate date format
            break
        except ValueError:
            print("Invalid date format! Please enter in YYYY-MM-DD format.")

    # Get valid end date
    while True:
        end_date = input("Enter end date (YYYY-MM-DD): ")
        try:
            pd.to_datetime(end_date)  # Validate date format
            if end_date >= start_date:  # Ensure end date is not before start date
                break
            else:
                print("End date must be after start date!")
        except ValueError:
            print("Invalid date format! Please enter in YYYY-MM-DD format.")

    # Convert "Date" column to datetime format
    data["Date"] = pd.to_datetime(data["Date"], errors="coerce")

    # Filter transactions within the given range
    filtered_data = data[(data["Date"] >= start_date) & (data["Date"] <= end_date)]

    if filtered_data.empty:
        print("\nNo transactions found in this date range.")
    else:
        print("\n--- Transactions from", start_date, "to", end_date, "---")
        print(filtered_data)
        print("\n--- End of Transactions ---")


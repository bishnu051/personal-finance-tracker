from data import load_data, save_data

def delete_transaction():
    """Delete a transaction by its index, with an option to cancel using '*'."""
    data = load_data("sampledata.csv")  # Load the latest transactions

    if data.empty:
        print("\nNo transactions found! Cannot delete.")
        return

    print("\n--- Current Transactions ---")
    print(data)

    while True:
        index_input = input("\nEnter transaction index to delete (* to Cancel): ")
        if index_input == "*":
            print("Transaction deletion canceled.")
            return

        try:
            index = int(index_input)
            if 0 <= index < len(data):
                break
            print("Invalid index! Please enter a valid row number.")
        except ValueError:
            print("Invalid input! Please enter a numeric index.")

    # Show transaction details before confirmation
    print("\n--- Transaction to Delete ---")
    print(data.iloc[index])

    # Confirm deletion
    confirm = input("\nAre you sure you want to delete this transaction? (y/n, * to Cancel): ").strip().lower()
    if confirm == "*":
        print("Transaction deletion canceled.")
        return

    if confirm == 'y':
        data.drop(index, inplace=True)  # Remove the row
        data.reset_index(drop=True, inplace=True)  # Reset index
        save_data(data, "sampledata.csv")  # Save updated data
        print("\nTransaction deleted successfully!")
    else:
        print("\nDeletion canceled.")


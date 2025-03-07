import pandas as pd

# function to load data wherever needed
def load_data(filename="sampledata.csv"):
    try:
        data = pd.read_csv(filename)
        return data
    except FileNotFoundError:
        print("Error: CSV file not found!")
        return pd.DataFrame()

# function to save edited data wherever needed
def save_data(data, filename="sampledata.csv"):
    data.to_csv(filename, index=False)
    print(f"Transactions saved to {filename} successfully!")

# function to export data
def export_data():
    data = load_data()
    filename = input("Enter the name for the data file to be saved")
    filename = filename + ".csv"
    data.to_csv(filename, index=False)
    print(f"Transactions saved to {filename} successfully!")

# function to view data
def view_data():
    data = load_data()
    print(data)


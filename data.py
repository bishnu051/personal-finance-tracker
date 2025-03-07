import pandas as pd

def load_data(filename="sampledata.csv"):
    try:
        data = pd.read_csv(filename)
        return data
    except FileNotFoundError:
        print("Error: CSV file not found!")
        return pd.DataFrame()

def save_data(data, filename="sampledata.csv"):
    data.to_csv(filename, index=False)
    print(f"Transactions saved to {filename} successfully!")

def view_data():
    data = load_data()
    print(data)

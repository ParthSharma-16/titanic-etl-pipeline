import pandas as pd

def validate_data(file_path):
    print(f"Loading {file_path}... \n")
    df = pd.read_csv(file_path)

    print("=== Shape ===")
    print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}\n")

    print("=== columns names and data types ===")
    print(df.dtypes, "\n")
    print()

    print("=== Missing values per column ===")
    print(df.isnull().sum())
    print()

    print("=== first 5 rows of the dataset ===")
    print(df.head())
    print()

    print("=== basic statistics of the dataset ===")
    print(df.describe())
    print()

if __name__ == "__main__":
    validate_data("raw_data.csv")

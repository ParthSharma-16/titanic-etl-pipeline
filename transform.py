import pandas as pd

def transform_data(file_path):

    print(f"Loading {file_path} for transformation ...\n")
    df = pd.read_csv(file_path)

   
    median_age = df["Age"].median()
    df["Age"] = df["Age"].fillna(median_age)
    print(f"filled {177} missing age values with median age : {median_age}")

    df["hasCabin"] = df["Cabin"].notnull().astype(int)
    df = df.drop(columns=["Cabin"])
    print("created column hasCabin instead of Cabin with flag 1 if cabin is present and 0 if not")

    most_common_port = df["Embarked"].mode()[0]
    df["Embarked"] = df["Embarked"].fillna(most_common_port)
    print(f"Filled missing Embarked values with most common port: {most_common_port}")

    print("\n=== missing values after cleaning ===")
    print(df.isnull().sum())

    return df

if __name__ == "__main__":
    cleaned_df = transform_data("raw_data.csv")
    cleaned_df.to_csv("cleaned_data.csv", index=False)
    print("\nCleaned data saved to 'cleaned_data.csv'.")
    
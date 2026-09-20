import pandas as pd
import sqlite3

def load_data(csv_filepath, db_filepath, table_name):
    print(f"Loading {csv_filepath} into {db_filepath} (table: {table_name})...\n")

    df = pd.read_csv(csv_filepath)
    conn = sqlite3.connect(db_filepath)

    df.to_sql(table_name, conn, if_exists='replace', index=False)
    print(f"loaded {len(df)} rows into table '{table_name}':\n")

    print("=== sample query : first 5 rows from the dataset ===")
    result = pd.read_sql_query(f"SELECT * FROM {table_name} LIMIT 5", conn)
    print(result)

    print("\n=== Sample query: survival rate by passenger class ===")
    result2 = pd.read_sql_query(f"""
        SELECT Pclass, AVG(Survived) as survival_rate, COUNT(*) as passenger_count
        FROM {table_name}
        GROUP BY Pclass
    """, conn)
    print(result2)

    conn.close()
    print("\n connection closed. Data is now in database.")

if __name__ == "__main__":
    load_data("cleaned_data.csv", "titanic.db", "passangers")
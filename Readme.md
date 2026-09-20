# Titanic ETL Pipeline

A basic ETL (Extract, Transform, Load) pipeline built in Python, using the Titanic dataset as sample data.

## Pipeline Steps
1. **Extract** (`extract.py`) — pulls raw CSV data from a public source into a staging file
2. **Validate** (`validate.py`) — profiles the raw data: shape, dtypes, missing values, summary stats
3. **Transform** (`transform.py`) — cleans the data:
   - Fills missing `Age` with median
   - Converts sparse `Cabin` column into a `HasCabin` flag
   - Fills missing `Embarked` with the most common port
4. **Load** (`load.py`) — loads cleaned data into a SQLite database and runs sample SQL queries

## Sample Output
Survival rate by passenger class (queried via SQL after loading):

| Pclass | Survival Rate | Passenger Count |
|--------|---------------|------------------|
| 1      | 0.63          | 216              |
| 2      | 0.47          | 184              |
| 3      | 0.24          | 491              |

## Tech Used
Python, pandas, SQLite, SQL

## How to Run
\`\`\`
python extract.py
python validate.py
python transform.py
python load.py
\`\`\`
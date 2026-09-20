import requests 
import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

def extract_data(url):

    print("Extracting data from the URL...")
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch data : Status code: {response.status_code}")

    with open("raw_data.csv", "wb") as f:
        f.write(response.content)

    print("Data extraction completed. Data saved to 'raw_data.csv'.")

if __name__ == "__main__":
    extract_data(url)
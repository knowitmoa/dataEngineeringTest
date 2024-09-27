import json
import pandas as pd
from sqlalchemy import create_engine
import psycopg2
import requests


def insert_to_tables():

    urlList = ['https://swapi.dev/api/people',
               'https://swapi.dev/api/planets', 'https://swapi.dev/api/starships']

    connection_string = 'postgresql://postgres_user:postgres_password@localhost:5432/starwars'
    engine = create_engine(connection_string)

    try:
        conn = psycopg2.connect(
            host='localhost',
            database='starwars',
            user='postgres_user',
            password='postgres_password'
        )
        cursor = conn.cursor()
        print("Database connection successful.")
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return

    for url in urlList:
        try:
            response = requests.get(url)
            response.raise_for_status()

            data = response.json()

            df = pd.DataFrame(data['results'])

            dbName = url.split('/')[4]

            df.to_sql(dbName, con=engine, if_exists='replace', index=False)

            print(dbName, "created and data inserted successfully!")

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

    engine.dispose()

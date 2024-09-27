import json
import pandas as pd
from sqlalchemy import create_engine
import psycopg2


def insert_to_tables():

    jsonList = ['persons_data.json',
                'planets_data.json', 'starships_data.json']

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

    for json_file in jsonList:
        with open(json_file) as f:
            data = json.load(f)

            dbName = json_file.split('_')[0]

            results = data.get('results', [])

            df = pd.DataFrame(results)

            if df.empty:
                print("No data to insert into the database.")
                continue

            df.to_sql(dbName, con=engine, if_exists='replace', index=False)

    engine.dispose()

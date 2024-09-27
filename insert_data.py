import pandas as pd
from sqlalchemy import create_engine
import requests


def insert_to_tables():

    urlAPI = 'https://swapi.dev/api/'
    response = requests.get(urlAPI)

    response.raise_for_status()

    data = response.json()

    connection_string = 'postgresql://postgres_user:postgres_password@localhost:5432/starwars'
    engine = create_engine(connection_string)

    for key, url in data.items():
        try:
            response = requests.get(url)
            response.raise_for_status()

            data = response.json()  # Gör jsonobjektet till en dictionairy
            # tar ut valuen som mappar till keyn 'results'
            resultData = data['results']

            # skapar en dataframe med resultData
            df = pd.DataFrame(resultData)

            df.to_sql(key, con=engine, if_exists='replace', index=False)

            print(key, "created and data inserted successfully!")

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

    engine.dispose()

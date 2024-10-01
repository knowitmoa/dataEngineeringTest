import pandas as pd
from sqlalchemy import create_engine
import requests

# import schedule
# import time


def insert_to_tables(connection_string):

    urlAPI = 'https://swapi.dev/api/'
    response = requests.get(urlAPI)

    response.raise_for_status()

    data = response.json()

    
    engine = create_engine(connection_string)
    totalDf = pd.DataFrame()

    for key, url in data.items():
        try:
            response = requests.get(url)
            response.raise_for_status()

            data = response.json()  # Gör jsonobjektet till en dictionairy
            # tar ut valuen som mappar till keyn 'results'
            resultData = data['results']

            # skapar en dataframe med resultData
            df = pd.DataFrame(resultData)

            totalDf = pd.concat([totalDf,df], axis=0)

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

    totalDf.to_sql('starWarsTable', con=engine, if_exists='replace', index=False)

    print('starWarsTable was created successfully!')
    


    engine.dispose()




    

   
    

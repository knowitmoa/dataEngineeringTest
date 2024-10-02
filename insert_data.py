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
    

    for key, url in data.items():
        for i in range(1,10):
            try:
                pageUrl= url+"?page="+str(i)
                print(pageUrl)
                response = requests.get(pageUrl)
                response.raise_for_status()

                data = response.json()  # Gör jsonobjektet till en dictionairy
                print(data)
                # tar ut valuen som mappar till keyn 'results'
                resultData = data['results']

                # skapar en dataframe med resultData
                df = pd.DataFrame(resultData)
                df.to_sql(key, con=engine, if_exists='append', index=False)
                print(  f"{key} was created successfully!")

            

            except requests.exceptions.HTTPError as http_err:
                print(f"HTTP error occurred: {http_err}")
            except Exception as err:
                print(f"An error occurred: {err}")
        
    

    
        engine.dispose()

def create_one_big_table(connectionString):
  
  engine = create_engine(connectionString)

  people_planets_df = pd.read_sql( '''SELECT people.name AS people_name, planets.name AS planets_name FROM people FULL OUTER JOIN planets ON people.films=planets.films;''', engine)
  

  people_planets_df.to_sql('total', con=engine , if_exists='replace', index=False)

  engine.dispose()



    

   



    

   
    

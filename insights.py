import pandas as pd
from sqlalchemy import create_engine

def insights (connectionString):

    engine = create_engine(connectionString)

   
    
    dfFilms = pd.read_sql('''SELECT name, 
       cardinality(string_to_array(trim(both '{}' from films), ',')) AS film_count,
       CASE 
           WHEN height IS NOT NULL THEN 'people'
           WHEN diameter IS NOT NULL THEN 'planet'
           WHEN average_height IS NOT NULL THEN 'species'
           WHEN length IS NOT NULL THEN 'Vehicle' 
           ELSE NULL 
       END AS definition
FROM "starWarsTable" ORDER BY film_count DESC;


''',engine)
    
    dfCleaned= dfFilms.dropna()


    engine.dispose()

    
    print(dfCleaned)

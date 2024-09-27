import requests
import json
import pandas as pd
from tables import *  # importrar metoder från andra filer.


urlPlanet = 'https://swapi.dev/api/planets'
urlPeople = 'https://swapi.dev/api/people'
urlStarships = 'https://swapi.dev/api/starships'


responsePlanet = requests.get(urlPlanet)
responsePeople = requests.get(urlPeople)
responseStarships = requests.get(urlStarships)


if responsePlanet.status_code == 200:

    dataPlanet = responsePlanet.json()

    with open('planet_data.json', 'w') as json_file:
        json.dump(dataPlanet, json_file, indent=4)

    print("Data saved to planet_data.json")
else:
    print(f"Failed to retrieve planets data. Status code: {
          responsePlanet.status_code}")


if responsePeople.status_code == 200:

    dataPeople = responsePeople.json()

    with open('persons_data.json', 'w') as json_file:
        json.dump(dataPeople, json_file, indent=4)

    print("Data saved to people_data.json")
else:
    print(f"Failed to retrieve persons data. Status code: {
          responsePeople.status_code}")


if responseStarships.status_code == 200:

    dataStarships = responseStarships.json()

    with open('starships_data.json', 'w') as json_file:
        json.dump(dataStarships, json_file, indent=4)

    print("Data saved to starships_data.json")
else:
    print(f"Failed to retrieve starships data. Status code: {
          responseStarships.status_code}")

    # main.py
createTables()
with open('insert_data.py') as insertData:
    exec(insertData.read())

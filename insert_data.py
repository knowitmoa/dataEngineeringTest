import json
import psycopg2


DB_HOST = 'localhost'
DB_NAME = 'starwars'
DB_USER = 'postgres_user'
DB_PASSWORD = 'postgres_password'


try:
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    cursor = conn.cursor()
    print("Database connection successful.")
except Exception as e:
    print(f"Error connecting to database: {e}")


with open('persons_data.json') as f:
    data = json.load(f)


for person in data['results']:
    films = person.get('films', [])
    species = person.get('species', [])
    vehicles = person.get('vehicles', [])
    starships = person.get('starships', [])

    cursor.execute(''' 
        INSERT INTO persons (
            name, height, mass, hair_color, skin_color, eye_color, birth_year, 
            gender, homeworld, films, species, vehicles, starships, created, edited, url
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ''', (
        person['name'],
        person['height'],
        person['mass'],
        person['hair_color'],
        person['skin_color'],
        person['eye_color'],
        person['birth_year'],
        person['gender'],
        person['homeworld'],
        films,
        species,
        vehicles,
        starships,
        person['created'],
        person['edited'],
        person['url']
    ))


with open('planet_data.json') as p:
    dataPlanets = json.load(p)


for planet in dataPlanets['results']:
    residents = planet.get('residents', [])
    films = planet.get('films', [])

    cursor.execute(''' 
        INSERT INTO planets (
            name, rotation_period, orbital_period, diameter, climate, gravity, terrain, 
            surface_water, population, residents, films, created, edited, url
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ''', (
        planet['name'],
        planet['rotation_period'],
        planet['orbital_period'],
        planet['diameter'],
        planet['climate'],
        planet['gravity'],
        planet['terrain'],
        planet['surface_water'],
        planet['population'],
        residents,
        films,
        planet['created'],
        planet['edited'],
        planet['url']
    ))

    with open('starships_data.json') as s:
        dataStarships = json.load(s)

    for starship in dataStarships['results']:
        pilots = starship.get('pilots', [])
        films = starship.get('films', [])

    cursor.execute(''' 
        INSERT INTO starships (
            name, model, manufacturer, cost_in_credits, length, max_atmosphering_speed, crew, 
            passengers, cargo_capacity,consumables, hyperdrive_rating,MGLT, starship_class,pilots,films,created, edited, url
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s)
    ''', (
        starship['name'],
        starship['model'],
        starship['manufacturer'],
        starship['cost_in_credits'],
        starship['length'],
        starship['max_atmosphering_speed'],
        starship['crew'],
        starship['passengers'],
        starship['cargo_capacity'],
        starship['consumables'],
        starship['hyperdrive_rating'],
        starship['MGLT'],
        starship['starship_class'],
        pilots,
        films,
        starship['created'],
        starship['edited'],
        starship['url']
    ))
print("Data inserted successfully.")
cursor.execute('''SELECT name FROM planets''')
data = cursor.fetchall()


print("Names of planets:")
for row in data:
    print(row[0])
conn.commit()
cursor.close()
conn.close()

import json
import psycopg2

# Database connection parameters
DB_HOST = 'localhost'
DB_NAME = 'starwars'
DB_USER = 'postgres_user'
DB_PASSWORD = 'postgres_password'

# Connect to PostgreSQL database
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

# Load JSON data from persons_data.json
with open('persons_data.json') as f:
    data = json.load(f)

# Insert data into the persons table
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

# Load JSON data from planets_data.json
with open('planet_data.json') as p:
    dataPlanets = json.load(p)

# Insert data into the planets table
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

#    Insert data into the planets table
    for star in dataStarships['results']:
        pilots = star.get('pilots', [])
        films = star.get('films', [])

    cursor.execute(''' 
        INSERT INTO starships (
            name, model, manufacturer, cost_in_credits, length, max_atmosphering_speed, crew, 
            passengers, cargo_capacity,consumables, hyperdrive_rating,MGLT, starship_class,pilots,films,created, edited, url
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s)
    ''', (
        star['name'],
        star['model'],
        star['manufacturer'],
        star['cost_in_credits'],
        star['length'],
        star['max_atmosphering_speed'],
        star['crew'],
        star['passengers'],
        star['cargo_capacity'],
        star['consumables'],
        star['hyperdrive_rating'],
        star['MGLT'],
        star['starship_class'],
        pilots,          # Correctly use the residents list from planet
        films,              # Directly pass the list to psycopg2
        star['created'],
        star['edited'],
        star['url']
    ))

cursor.execute('''SELECT name FROM planets''')
data = cursor.fetchall()

# Print each planet name on a new line
print("Names of planets:")
for row in data:
    print(row[0])
conn.commit()
cursor.close()
conn.close()

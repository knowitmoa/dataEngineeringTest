from sqlalchemy import create_engine


def createTables():
    engine = create_engine(
        'postgresql://postgres_user:postgres_password@localhost:5432/starwars')
    print("inne i tables")

    with engine.begin() as conn:
        conn.exec_driver_sql("DROP TABLE IF EXISTS persons;")
        conn.exec_driver_sql("DROP TABLE IF EXISTS planets;")
        conn.exec_driver_sql("DROP TABLE IF EXISTS starships;")
        conn.exec_driver_sql('''CREATE TABLE IF NOT EXISTS persons (name TEXT, 
                             height TEXT, mass TEXT, 
                             hair_color TEXT,skin_color TEXT,
                             eye_color TEXT,birth_year TEXT,gender TEXT,
                             homeworld TEXT, films TEXT[],  
                             species TEXT[],vehicles TEXT[],
                             starships TEXT[],
                             created TEXT,
                             edited TEXT,
                             url TEXT);''')
        conn.exec_driver_sql("""CREATE TABLE IF NOT EXISTS planets (name TEXT, 
                             rotation_period TEXT, 
                             orbital_period TEXT, 
                             diameter TEXT, 
                             climate TEXT, 
                             gravity TEXT, 
                             terrain TEXT, 
                             surface_water TEXT, 
                             population TEXT, 
                             residents TEXT[], 
                             films TEXT[], 
                             created TEXT, 
                             edited TEXT, 
                             url TEXT);""")
        conn.exec_driver_sql("""CREATE TABLE IF NOT EXISTS starships (name TEXT, 
                             model TEXT, 
                             manufacturer TEXT, 
                             cost_in_credits TEXT, 
                             length TEXT, 
                             max_atmosphering_speed TEXT, 
                             crew TEXT, passengers TEXT, 
                             cargo_capacity TEXT, 
                             consumables TEXT, 
                             hyperdrive_rating TEXT, 
                             MGLT TEXT, 
                             starship_class TEXT, 
                             pilots TEXT[],
                             films TEXT[], 
                             created TEXT, 
                             edited TEXT, 
                             url TEXT);""")

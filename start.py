from insert_data import *
from insights import *
import os
from dotenv import load_dotenv

load_dotenv()

MY_POSTGRES_USER = os.getenv('MY_POSTGRES_USER')
MY_POSTGRES_PASSWORD =os.getenv('MY_POSTGRES_PASSWORD')
MY_POSTGRES_DATABASE = os.getenv('MY_POSTGRES_DATABASE')


connectionString = f'postgresql://{MY_POSTGRES_USER}:{MY_POSTGRES_PASSWORD}@localhost:5432/{MY_POSTGRES_DATABASE}'

insert_to_tables(connectionString)
create_one_big_table(connectionString)

# insights(connectionString)





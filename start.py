from insert_data import *
from insights import *




connectionString = 'postgresql://postgres_user:postgres_password@localhost:5432/starwars'

insert_to_tables(connectionString)

insights(connectionString)





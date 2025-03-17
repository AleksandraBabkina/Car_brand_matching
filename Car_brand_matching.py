from sqlalchemy import create_engine, Column, String, Float, select, or_, and_, Table, MetaData, inspect, text, types
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.dialects import oracle
import pandas as pd
import sys
import oracledb
import pandas as pd
import re
from fuzzywuzzy import fuzz, process
pd.set_option('display.max_rows', None)

oracledb.version = "8.3.0"
sys.modules["cx_Oracle"] = oracledb

# Header with connection DO NOT MODIFY
username = 'username'
password = 'password'
dsn = 'dsn'

conection_string = f'oracle+cx_oracle://{username}:{password}@{dsn}' # Opening SQL connection
engine = create_engine(conection_string) # Engine

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Define query
query = """
select a.CATEGORY, a.mark|| ' ' || a.model model from diasoft_test.v_category_mark_model a
"""

# Execute query and load data into variable all_city_RF
all_molel_ts = pd.read_sql_query(query, engine)
all_molel_ts.head()

# Define query
query = """
select КАТЕГОРИЯ, BRAND_MODEL from al_babkina_bs_ts_2021_2024 where type_t = '!ошибка'
"""

# Execute query and load data into variable all_city_RF
my_ts = pd.read_sql_query(query, engine)

# Close connection to the database
engine.dispose()
my_ts

my_ts['the_same_model'] = my_ts['brand_model'].apply(lambda x: x if x in all_molel_ts['model'].values else '')
my_ts['category'] = my_ts['the_same_model'].apply(lambda x: all_molel_ts.loc[all_molel_ts['model'] == x, 'category'].iloc[0] if x in all_molel_ts['model'].values else '')
my_ts

df = my_ts
for index, row in df.iterrows():
    if row['category']!= '':
        print(f"UPDATE al_babkina_bs_ts SET КАТЕГОРИЯ = '{row['category']}' where BRAND_MODEL = '{row['the_same_model']}';")
        
print("select * from al_babkina_bs_ts_2021_2024 where BRAND_MODEL in (")
for index, row in df.iterrows():
    if row['category']!= '':
        print(f" '{row['the_same_model']}',")
print(") and TYPE_T = '!ошибка'")

print("select * from al_babkina_bs_ts_2021_2024 where BRAND_MODEL in (")
for index, row in df.iterrows():
    if row['category']!= '':
        print(f" '{row['the_same_model']}',")
print(") and TYPE_T = '!ошибка'")

my_ts = my_ts.assign(the_same_model='')
for index, row in my_ts.iterrows():
    brand = row['brand_model']
    if isinstance(brand, str):  # check if city_ru is a string
        match = process.extractOne(brand, all_molel_ts['model'], scorer=fuzz.ratio)
        if match:
            my_ts.loc[index, 'the_same_model'] = match[0]

my_ts['category'] = my_ts['the_same_model'].apply(lambda x: all_molel_ts.loc[all_molel_ts['model'] == x, 'category'].iloc[0] if x in all_molel_ts['model'].values else '')
my_ts

my_ts = my_ts.assign(the_same_model='')
for index, row in my_ts.iterrows():
    brand = row['brand_model']
    if isinstance(brand, str):  # check if city_ru is a string
        match = process.extractOne(brand, all_molel_ts['model'], scorer=fuzz.token_set_ratio)
        if match:
            my_ts.loc[index, 'the_same_model'] = match[0]

my_ts['category'] = my_ts['the_same_model'].apply(lambda x: all_molel_ts.loc[all_molel_ts['model'] == x, 'category'].iloc[0] if x in all_molel_ts['model'].values else '')
my_ts

with session.begin():
    station.to_sql('', engine, if_exists='append', index=False)
    session.commit()

session.close()
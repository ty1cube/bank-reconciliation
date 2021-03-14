import os
import pyodbc 
import pandas as pd
import numpy as np
from dotenv import load_dotenv

load_dotenv()

# Database configuration
# server = os.getenv('SERVER')
# database = os.getenv('DB_NAME')
# username = os.getenv('DB_USERNAME')
# password = os.getenv('DB_PASSWORD')

#connect to the Database
# connection = pyodbc.connect(
#         'DRIVER={ODBC Driver 17 for SQL Server};\
#         SERVER='+server+';\
#         DATABASE='+database+';\
#         UID='+username+';\
#         PWD='+ password
#         )
# cursor = connection.cursor()
# print(cursor)

# df = pd.read_sql_query('SELECT * FROM [DB_114226_vsdsandbox].[dbo].[bank_statement_activity]', connection)
# print(df)

server = os.getenv('SERVER')
# database = os.getenv('DB_NAME')
username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
    

def create_db_connection(server,username, password):
    connection = None
    try:
        connection = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};\
            SERVER='+server+';\
            UID='+username+';\
            PWD='+ password
        )
        print("Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

conn = create_db_connection(server,username,password)
print(conn)


df = pd.read_sql_query(
    'SELECT * FROM [DB_114226_vsdsandbox].[dbo].[Bank_Ledger_Transactions]', conn)
print(df)


def read_db_table(dbname, **kwargs):
    pass

def all_table_matches():
    pass

def at_least_three_matching_values():
    pass

def not_at_least_three_matching_values():
    pass
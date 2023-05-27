import os
import pandas as pd
import csv
from sqlalchemy import create_engine
import psycopg2
import sys
from config import param_dic

def write_to_csv(data, filename):
    # filename = 'wildberries_data_test.csv'
    columns = ['id_on_store','brand',"title", "price",'url', 'description', 'specifications','marketplace','category']
    if os.path.isfile(filename):
        with open (filename,"a", encoding="utf-8", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writerow(data)
    else:
        with open (filename,"w", encoding="utf-8", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writeheader()
            # print(data)
            writer.writerow(data)

def connect(params_dic):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params_dic)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1) 
    print("Connection successful")
    return conn

def save_to_db(df,table_name):
    connect = "postgresql+psycopg2://%s:%s@%s:5432/%s" % (
        param_dic['user'],
        param_dic['password'],
        param_dic['host'],
        param_dic['database'])
    engine = create_engine(connect)
    df.to_sql(
        table_name, 
        con=engine, 
        index=False, 
        if_exists='append'
    )
    print("to_sql() done (sqlalchemy)")
    
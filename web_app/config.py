import psycopg2
import torch
from sqlalchemy import create_engine

cols = ['id','brand','title','price','description','specifications','category','marketplace','url','stars','sku']


def get_db_connection():
    conn = psycopg2.connect(host='84.201.175.11',
                            database='wishlist',
                            user='web_app',
                            password='shopsdb9274')
    return conn



# написать ф-ю, которая будет подключаться к бд, а как аргумент принимает sql запрос
def get_data_from_db(query, params):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(query,params)
    cur.close()
    conn.close()
    data = cur.fetchall()
    return data

param_dic = {
    "host"      : "84.201.175.11",
    "database"  : "wishlist",
    "user"      : "web_app",
    "password"  : "shopsdb9274"
}

connect = "postgresql+psycopg2://%s:%s@%s:5432/%s" % (
    param_dic['user'],
    param_dic['password'],
    param_dic['host'],
    param_dic['database']
)


def to_db(df,table_name):
    """
    Using a dummy table to test this call library
    """
    engine = create_engine(connect)
    df.to_sql(
        table_name, 
        con=engine, 
        index=False, 
        if_exists='append'
    )
    print("to_sql() done (sqlalchemy)")
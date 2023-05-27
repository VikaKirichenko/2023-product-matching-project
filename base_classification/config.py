import psycopg2

def get_db_connection():
    conn = psycopg2.connect(host='84.201.175.11',
                            database='wishlist',
                            user='web_app',
                            password='shopsdb9274')
    return conn
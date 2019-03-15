import psycopg2 #import the psycopg2 module for running PostgreSQL queries

def get_reports():
    db = psycopg2.connect("dbname=news") #connect to news database
    cur = db.cursor() #create a new cursor from database

    cur.execute("SELECT * FROM authors LIMIT 2;")

    return cur.fetchall()
    db.close()

print(get_reports())
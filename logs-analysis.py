import psycopg2 #import the psycopg2 module for running PostgreSQL queries

def get_reports():
    db = psycopg2.connect("dbname=news") #connect to news database
    cur = db.cursor() #create a new cursor from database

    cur.execute("SELECT * FROM authors;")

    return cur.fetchall()
    db.close()

for i in range(len(get_reports())):
    print(get_reports()[i][0])
    print("\n")
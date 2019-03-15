# Import the psycopg2 module for running PostgreSQL queries.
import psycopg2

# Function to retrieve 3 most popular articles from database.
def get_popular_articles():
    
    # Connect to news database and create a new cursor.
    db = psycopg2.connect("dbname=news")
    cur = db.cursor()

    # Query the popular_articles view to retrieve 3 most popular queries.
    cur.execute("SELECT * FROM popular_articles;")

    # Return the most popular articles and close connection to database.
    return cur.fetchall()
    db.close()

print(get_popular_articles())

#!/usr/bin/python3

# Import the psycopg2 module for running PostgreSQL queries.
import psycopg2


# Function to retrieve all 3 reports
def retrieve_reports():
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

    # Function to retrieve 3 most popular authors from database.
    def get_popular_authors():

        # Connect to news database and create a new cursor.
        db = psycopg2.connect("dbname=news")
        cur = db.cursor()

        # Query the popular_authors view to retrieve 3 most popular authors.
        cur.execute("SELECT * FROM popular_authors;")

        # Return most popular authors and close the connection to the database.
        return cur.fetchall()
        db.close()

    # Function to retrieve days where error rates were >1%.
    def get_error_rates():

        # Connect to news database and create a new cursor.
        db = psycopg2.connect("dbname=news")
        cur = db.cursor()

        # Query the error_rates view to retrieve days with >1% error rates.
        cur.execute("SELECT * FROM error_rates;")

        # Return days with >1% errors and close the connection to the database.
        return cur.fetchall()
        db.close()

    # Iterate over get_popular_articles() list and print out results
    print('The most popular articles are:')
    for i in range(len(get_popular_articles())):
        print(
            '*', get_popular_articles()[i][0],
            '-', get_popular_articles()[i][1],
            'views')

    print('\n')

    # Iterate over get_popular_authors() list and print out results
    print('The most popular authors are:')
    for i in range(len(get_popular_authors())):
        print(
            '*', get_popular_authors()[i][0],
            '-', get_popular_authors()[i][1],
            'views')

    print('\n')

    # Iterate over get_error_rates() list and print out results
    print('Days with error rates >1%:')
    for i in range(len(get_error_rates())):
        print(
            '*', get_error_rates()[i][0],
            '-', get_error_rates()[i][1])


retrieve_reports()

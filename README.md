# Logs Analysis Project

This program was created for the Udacity Full Stack Engineering Nanodegree and satisfies all the requirements of the logs analysis project.

Running this script will allow you to retrieve the following 3 reports from the 'news' database:

- Most popular three articles of all time
- Most popular article authors of all time
- Days where more than 1% of requests lead to errors

The program uses 3 functions (get_popular_articles(), get_popular_authors(), get_error_rates()) to query the 'news' database and retrieve each report, all of which are nested under a primary retrieve_reports() function which executes the 3 functions and prints out the results.

## Requirements

- [Python 3](https://www.python.org/downloads/)
- [psycopg](http://initd.org/psycopg/) (required for connecting to PostgreSQL database and executing queries)

## Usage

From your command line, navigate to the directory where you saved the file logs-analysis.py and run the following command:

`$ python3 logs-analysis.py`

After running the command above, you should see the following plain text output in your terminal:

```text
The most popular articles are:
* Candidate is jerk, alleges rival - 338647 views
* Bears love berries, alleges bear - 253801 views
* Bad things gone, say good people - 170098 views


The most popular authors are:
* Ursula La Multa - 507594 views
* Rudolf von Treppenwitz - 423457 views
* Anonymous Contributor - 170098 views
* Markoff Chaney - 84557 views


Days with error rates >1%:
* July 17, 2016 - 2.3% errors
```

## PostgreSQL views created to query the data

The following views were created in PostgreSQL to simplify the SQL queries in the Python code.

Please use the following queries to recreate the views for yourself:

#### Popular Articles view

```sql
CREATE VIEW popular_articles AS
    SELECT articles.title, COUNT(log.path) AS views 
    FROM articles, log
    WHERE log.path = format('/article/%s', articles.slug)
    GROUP BY articles.title
    ORDER BY views DESC
    LIMIT 3;
```
#### Popular Authors view

```sql
CREATE VIEW popular_authors AS
    SELECT authors.name, COUNT(log.path) AS views
    FROM articles, authors, log
    WHERE log.path = format('/article/%s', articles.slug) AND authors.id = articles.author
    GROUP BY authors.name
    ORDER BY views DESC;
```

#### Error Rates view

```sql
CREATE VIEW error_rates AS
    SELECT totals.day, round(errors.error_count/totals.count_of_codes::numeric * 100, 1)::text || '% errors' AS percent_of_errors
    FROM (
        SELECT to_char(date(time), 'FMMonth DD, YYYY') AS day, COUNT(status) AS count_of_codes 
        FROM log
        GROUP BY day
        ORDER BY day
    ) AS totals
    JOIN (
        SELECT to_char(date(time), 'FMMonth DD, YYYY') AS day, COUNT(status) AS error_count
        FROM log
        WHERE status = '404 NOT FOUND'
        GROUP BY day
        ORDER BY day
    ) AS errors
    ON totals.day = errors.day
    WHERE errors.error_count/totals.count_of_codes::numeric * 100 > 1;
```
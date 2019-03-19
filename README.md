# Logs Analysis Project

This program was created for the Udacity Full Stack Engineering Nanodegree and satisfies all the requirements of the logs analysis project.

Running this script will allow you to retrieve the following 3 reports from the 'news' database:

- Most popular three articles of all time
- Most popular article authors of all time
- Days where more than 1% of requests lead to errors

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
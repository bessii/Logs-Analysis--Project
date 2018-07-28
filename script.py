#!/usr/bin/env python
import psycopg2


def connect(dbname="news"):
    """Commence by connecting to the PostgreSQL database"""
    try:
        db = psycopg2.connect("dbname={}".format(dbname))
        c = db.cursor()
        return db, c
    except:
        print("Something went wrong! Can't connect to database")

    """SQL queries to generate results for each respective task"""
task1 = '***The three most popular articles of all time?--'
request_top_articles = """
    select title, count(*) as views from articles inner join
    log on concat('/article/', articles.slug) = log.path
    where log.status like '%200%'
    group by log.path, articles.title order by views desc limit 3; """

task2 = '***The most popular article authors of all time?--'
request_top_authors = """
    select authors.name, count(*) as views from articles inner join
    authors on articles.author = authors.id inner join
    log on concat('/article/', articles.slug) = log.path where
    log.status like '%200%' group by authors.name order by views desc; """

task3 = '***Which days did more than 1% of requests lead to errors?--'
request_error_days = """
    select day, percentage from 
    (select day, round((sum(views)/(select count(*) from log where 
    substring(cast(log.time as text), 0, 11) = day) * 100), 2) as 
    percentage from (select substring(cast(log.time as text), 0, 11) as day, 
    count(*) as views from log where status like '%404%' group by day)
    as log_percentage group by day order by percentage desc) as final
    where percentage >= 1.0; """

""" Function returns results generated from the queries"""


def get_results(sql_request):
    db, c = connect()

    c.execute(sql_request)
    results = c.fetchall()
    db.close()
    return results

"""Function to output results on screen"""


def print_results(task, request_results):
    print('')
    print(task)
    for results in request_results:
        print ('\t' + str(results[0]) )


def print_error_days(task, request_results):
    print('')
    print(task)
    for result in request_results:
        print ('\t' + str(result[0]) + '   =  ' + str(result[1]) + 'percent')

"""the scope in which the main program executes"""
if __name__ == '__main__':

    top_articles = get_results(request_top_articles)
    top_authors = get_results(request_top_authors)
    high_error_days = get_results(request_error_days)

    print_results(task1, top_articles)
    print_results(task2, top_authors)
    print_error_days(task3, high_error_days)
    print "\n Mission Complete! \n" 
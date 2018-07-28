# Logs Analysis Project

## Description

We will be exploring the world of SQL databases and how to connect to a database with Python. We have been provided with an enormous database from a newspaper website and we will be executing complex queries on a large database of more than 500k rows to extract interesting statistics answering the following questions:
   1.What are the most popular three articles of all time?
   2.Who are the most popular article authors of all time?
   3.On which days did more than 1% of requests lead to errors?


i will be using a single query to answer each of the questions then use python to print the results out in plain text. See [script.py](script.py) for more details.

The database has 3 tables; `articles`, `authors` and `log`.
* `articles` - Contains articles which have been posted in the newspaper so far.
* `authors` - Contains the list of authors who have published their articles.
* `log` - Stores a log of every request sent to the newspaper server.

This project implements a single query solution for each of the question in hand.


## Setup

1. Download and Install
   - Vagrant  (https://www.vagrantup.com/downloads.html)
   - Virtual Box  (https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) 

2. Clone the Full Stack Nanodegree course's VM setup from here (https://github.com/udacity/fullstack-nanodegree-vm)

## Running

* Download `newsdata.sql`, the SQL script file with all the data. (https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

* Next, run the following command to load the database

```sh
psql -d news -f newsdata.sql
```

* Finally run the script.

```sh
python script.py
```

* It should present you with necessary stats. Something like this
![output image](/logs_output.png)


ps: its a large database so the script might take some time to produce the results ... be patient :-)
----
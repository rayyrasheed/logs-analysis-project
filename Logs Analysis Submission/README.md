# Project Name:
Logs Analysis

# Project Desscription:
SQL queries to retreive data


# Required views to run the project:

create view nameslug as
select name, slug from articles join authors
on articles.author = authors.id;

create view liststatus as 
select status, cast(time as date) as time,
count(*) as num from log
group by status, cast(time as date)
order by cast(time as date);


# Procedure to run program:
1. Open your VM or server
2. Connect to the news.py by running command: python news.py
3. watch the results
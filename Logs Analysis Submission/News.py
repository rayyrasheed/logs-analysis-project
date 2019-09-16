import psycopg2

# Connect to an existing database
db = psycopg2.connect(database="news")


# Open a cursor to perform database operations
cur = db.cursor()



cur.execute("select title, count(*) as num from log join articles on log.path like concat ('%', articles.slug, '%') group by title order by num desc limit 3;")
rows=cur.fetchall()
print
print "Top Three Articles:"
for row in rows:
    print "  ", row[0], "--", row[1], "views"

db.commit()

cur.execute( "select name, count(*) as num from nameslug join log on log.path like concat('%', nameslug.slug, '%') group by name order by num desc limit 3;")
rows=cur.fetchall()
print
print "Top authors of all time:"
for row in rows:
    print "  ", row[0], "--", row[1], "views"

cur.execute("select a.time as date, concat(trunc(cast( (cast(b.num as float) / (cast(a.num as float) + cast(b.num as float))*100) as numeric),2),'%') as percent from liststatus a join liststatus b on a.status='200 OK' and b.status ='404 NOT FOUND' and a.time=b.time and cast(b.num as float)/(cast(a.num as float)+cast(b.num as float))>0.01;")
rows=cur.fetchall()
print
print "Days with errors over 1%:"
for row in rows:
    print "  ", row[0], "--", row[1], "errors"


# Close communication with the database
cur.close()
db.close()
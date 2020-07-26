from mysql import connector as c

con = c.connect(host='localhost',user='shree',password='shree@123')
cur = con.cursor()
cur.execute("show databases;")
for i in cur:
    print(list(i))
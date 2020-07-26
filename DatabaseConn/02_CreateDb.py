from mysql import connector as c

connection = c.connect(host='localhost',user='shree',password='shree@123')
curser = connection.cursor()
curser.execute("create database NAMES")
curser.execute("use NAMES")
curser.execute("create table names_det(names varchar(30));")
curser.execute("insert into names_det values('Ganya');")
for x in curser:
    print(x)
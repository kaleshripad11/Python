#### Import connector class
from mysql import connector

#### Create connector object
conobj = connector.connect(host='localhost',user='shree',password='shree@123')

#### Create cursor object to store records from databases
curser = conobj.cursor()

#### Get databases names using execute() method
curser.execute("show databases;")

#### Iterate through the results
for i in curser:
    print(list(i))

#### Get the database name
dbname = input("Enter the name of database to be dropped(Name must be from above list) : ")
curser.execute("drop database {0};".format(dbname))

conobj.close()
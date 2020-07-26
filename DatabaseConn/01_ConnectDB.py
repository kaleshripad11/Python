## Import mysql package
from mysql import connector

## Create connection object
connection = connector.connect(host='localhost',user='myuser',password='user@123',database='dummy_db')
if connection.is_connected():
    info = connection.get_server_info()
    print(info)
    print('Connection succeeded...')
print('Closing connection...')
connection.close()
print(connection)



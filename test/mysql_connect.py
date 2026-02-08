import mysql.connector

cnx = mysql.connector.connect(
    user='root',
    password='legedawn0133',
    host='localhost',
    port='13306'
)
cursor = cnx.cursor()
cursor.execute('SELECT * FROM hoge_db.users;')

for id, name in cursor:
    print(f'{id}: {name}' )

# pip install mysql-connector-python

import mysql.connector

# connect:

connection = mysql.connector.connect(user='root', password='root12#', host='127.0.0.1',
                                     database='sql_kurs_1', auth_plugin='mysql_native_password')

# select:

query = 'SELECT username, display_name, year_of_birth FROM users'

cursor = connection.cursor()

#cursor.execute(query)
#for row in cursor:
    #print(row)

cursor.execute(query)
for (username, display_name, year_of_birth) in cursor:
    print(f'{username} - {display_name} - {year_of_birth}')

# insert:

insertQuery = "INSERT INTO users(username, display_name, year_of_birth) VALUES(%(username)s, %(display_name)s, %(year_of_birth)s)"

insertData = {
    'username' : 'dorota333',
    'display_name' : 'dorota janiak',
    'year_of_birth' : '1983'
}

cursor.execute(insertQuery, insertData)
connection.commit()
connection.close()





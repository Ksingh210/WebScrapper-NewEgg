import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='django1234',
                                         database='amazonwebscrapperdb')
except Error as e:
    print("Error while connecting to MySQL", e)
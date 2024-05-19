import mysql.connector

connection = mysql.connector.connect(
    user='root', password='root', host='mysql', port="3306", database='db')
print("DB connected")

connection.close()
cursor = connection.cursor()

aviao_id = 1
aviao_modelo = 'Boeing 737'

insert_query = """
INSERT INTO aviao (id, modelo)
VALUES (%s, %s)
"""
cursor.execute(insert_query, (aviao_id, aviao_modelo))
connection.commit()

cursor.execute('Select * FROM aviao')
avioes = cursor.fetchall()
print(avioes)
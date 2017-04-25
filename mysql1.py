import pymysql


client = pymysql.connect(host='127.0.0.1', user='root', password='tiger', db='practice')
cursor = client.cursor()
query = 'CREATE TABLE  days ( morning  VARCHAR(120), afternoon DATETIME);'
#query = 'INSERT INTO em(id,Name,Surname,age) values(6,"phani","k",26);'
query1 = 'show tables ;'
#cursor.execute(query)
query3 = ' describe days;'
cursor.execute(query3)
data=cursor.fetchall()
print(data)
client.close()

		

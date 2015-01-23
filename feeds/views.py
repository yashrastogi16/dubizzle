# from django.shortcuts import render
import MySQLdb
# Create your views here.

conn = MySQLdb.connect(host="127.0.0.1",
	user="root",
	passwd="1234",
	db="school")
mysqlcur = conn.cursor()
mysqlcur.execute("SELECT * FROM student")
abc = mysqlcur.fetchall()
for i in abc:
	for x in i:
		print x
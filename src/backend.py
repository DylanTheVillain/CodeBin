import MySQLdb as db
import cgi
import os
import sys

print "Content-Type: text/html\n"
try:
	con=db.connect('localhost','johnsondy','password','johnsondy')
	cur=con.cursor()
except db.Error, e:
	print e 
	sys.exit(1)

form=cgi.FieldStorage()

if (int(form['pick'])==1):
	cur.execute("SELECT filename FROM filetable WHERE filename=%s",str(form['file'].value))
	con.commit()
	fileName=cur.fetchall()
	if (len(fileName)==0):
		print "This file no longer exists."
	else:
		fi=open(str(form['file'].value)+".txt","r")
		for line in fi:
			print line
		fi.close()

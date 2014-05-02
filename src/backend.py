import MySQLdb as db
import cgi
import os
import sys

print "Content-Type: text/html\n"
try:
	con=db.connect("johnsondy","localhost","johnsondy","password")
	cur=con.cursor()
except db.Error, e:
	print e 
	sys.exit(1)

form=cgi.FieldStorage()
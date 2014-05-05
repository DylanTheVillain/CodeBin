import MySQLdb as db
import cgi
import os
import sys
import shutil
import datetime
import time
import hashlib
from random import randrange

print "Content-Type: text/html\n"
try:
	con=db.connect('localhost','johnsondy','password','johnsondy')
	cur=con.cursor()
except db.Error, e:
	print e 
	sys.exit(1)

form=cgi.FieldStorage()

def GenFileName():
	ti=time.time()
	ts=datetime.datetime.fromtimestamp(ti).strftime('%Y-%m-%d %H:%M:%S')
	tsString=str(ts)
	tsHash=hashlib.sha224(tsString).hexdigest()
	tsHash=str(tsHash)
	fiName=""
	while (True):
		fiName=""
		for x in range(0,10,1):
			hashDig=randrange(0,len(tsHash)-1)
			fiName+=tsHash[hashDig]
		cur.execute("SELECT COUNT(filename) FROM filetable WHERE filename=%s",fiName)
		count=con.commit()
		if (count==None):
			cur.execute("INSERT INTO `filetable`(`filename`, `filehash`, `lastaccess`) VALUES (%s,%s,%s)",(fiName,tsHash,ts))
			con.commit()
			break



if (int(form['pick'].value)==1):
	GenFileName()

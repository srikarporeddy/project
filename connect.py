#import mysql 
'''
import MySQLdb
myConnection = MySQLdb.connect( host=localhost, user=root, passwd=tiger, db=database )
doQuery( myConnection )
myConnection.close()

print "Using pymysql…"
import pymysql
myConnection = pymysql.connect( host=hostname, user=username, passwd=password, db=database )
doQuery( myConnection )
myConnection.close()
'''
print "Using mysql.connector…"
import mysql.connector
myConnection = mysql.connector.connect( host=localhost, user='root', passwd='tiger', db='pract' )
doQuery( myConnection )
myConnection.close()


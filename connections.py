# Collect values from form

import pymysql


client = pymysql.connect(host='127.0.0.1', user='root', password='tiger', db='practice')
inputs = cgi.FieldStorage()
fill = {}
for key in inputs:
   fill[key] = inputs[key].value

# If the form was completed, save what was entered on it
try:
     said = fill["info"]
     form = 1
     db.query('insert into comment (info) values ("' \
               +said.replace('"',r'\"') \
               +'")')
except:
     form = 0

# Read back 10 latest comments
db.query("SELECT info FROM comment order by cid desc limit 10")
r = db.store_result()

history = ""
for row in r.fetch_row(10):
    history += cgi.escape(row[0]) + "<br>\n"

# Generate the HTML response

#######################################################
'''
print """content-type: text/html

<html><head><title>MySQL and Python on the Web</title></head>
<body bgcolor=#FFCCFF><h1>Message Board Report</h1>
This is a message board report demo.<hr>
<b>This is what has been going on ... </b><br>
"""

print history

print """
<hr>
<form method=POST>Please enter your comment: <input name=info><br>
<input type=submit>
</form>
<hr>
Demonstration from Well House Consultants.<br>
<a href=http://www.wellho.net/>Website</a>
</body></html>
"""

''' 
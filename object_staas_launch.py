#!/usr/bin/python36

print("content-type: text/html")
print("")

import subprocess as sp
import cgi
print("Choose your Service")

print("""
<form action='saas-launch.py'>
<select name='choice'>
<option>SAAS</option>
<option>STAAS</option>
<option>PAAS</option>
<input type='submit' />
""")

file = cgi.FieldStorage()
date = file.getvalue('choice')

if data == 'SAAS':
	print('Service started' + '<a href="saas-launch.py">Click here to manage the service</a>')



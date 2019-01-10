#!/usr/bin/python36

print("content-type: text/html")
print("")


import cgi
import subprocess as sp

form=cgi.FieldStorage()
#username=form.getvalue('username')
#software=form.getvalue('software')
#print(username)

#x=sp.getstatusoutput("python36 /var/www/cgi-bin/signup.py")
#print(x)
#if x[0]==0:
#   print("successful signup")
#else:
#   print("Not Provided")




print("1. signup\n2. login")
c= intput("enter choice")
if int(c)==1:
	print("show face on camera")
        a=sp.getstatusoutput("python36 /var/www/cgi-bin/signup.py")
        print(a)
elif int(c)==2:
        print("login......")
        sp.getstatusoutput("python36 /var/www/login.py")
else:
        print("wrong choice")

import subprocess as sp
import cgi

print("content-type: text/html")

form = cgi.FieldStorage()
cname = form.getvalue('x')

o = sp.getstatusoutput("python36 /var/www/cgi-bin/signup.py")

if o[0] == 0:
        print("location: docker-manage.py")
        print("")


else:
        print("location: docker-manage.py")
        print("")

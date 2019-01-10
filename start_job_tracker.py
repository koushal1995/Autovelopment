#!/usr/bin/python36

print("content-type: text/html")
print("")

import cgi
import subprocess as sp

form  = cgi.FieldStorage()
ip_job = form.getvalue("jobtrackers")

print(ip_job)

#setup = sp.getstatusoutput('sudo ansible-playbook installation_hadoop.yml')

#print(setup)

start_job_tracker = sp.getstatusoutput("sudo ansible-playbook /root/Ansible_playbooks/jt.yml --extra-vars='ip={}'".format(ip_job))
print(start_job_tracker)

if start_job_tracker[0] ==0:
	print("Jobtracker started successfully...")
	print("""
	<form action='http://192.168.43.251:50030'>
	<button type='submit'>WebGUI of JT</button>
	</form>
	""")
else:
	print("error in  jobtracker...")
	exit()

#!/usr/bin/python36

print("content-type: text/html")
print("")

import cgi
import subprocess as sp

form = cgi.FieldStorage()
ips = form.getvalue('tt1')
#ips = form.getvalue('ips')

#ips = ips.split(",")
print(ips)

#for i in ips:
#setup_datanodes = sp.getstatusoutput('sudo ansible-playbook /root/Ansible_playbooks/installation_hadoop.yml')
#print(setup_datanodes)
start_tasktrackers = sp.getstatusoutput("sudo ansible-playbook /root/Ansible_playbooks/tt.yml --extra-vars='ip={}'".format(ips))
print(start_tasktrackers)
if start_tasktrackers[0] ==0:
	print("tasktrackers succesfully started...")
	print("<a href='http://192.168.43.251:50030'>Click here to get WebGUI of Datanode</a>")
else:
	print("starting datanodes failed.")
	exit()

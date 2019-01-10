#!/usr/bin/python36

print("content-type: text/html")
print("\n")

import cgi
import subprocess as sp

form = cgi.FieldStorage()
ip_name = form.getvalue("namenode")
print(ip_name)
#if ip_name == "192.168.43.108":
#conf_name_node = sp.getstatusoutput('ansible-playbook /root/Ansible_playbooks/installation_hadoop.yml')
#if conf_name_node[0] == 0:
#	print("installation successfull...")
#else:
#	print("installation failed...")
#	exit()
start_name_node = sp.getstatusoutput('sudo ansible-playbook /root/Ansible_playbooks/namenode.yml --extra-vars="ip={}"'.format(ip_name))
print(start_name_node)
if start_name_node[0] ==0:
	print("Namenode started successfully...")
else:
	print("Namenode start failed...")
	exit()
print("""
<form action='http://192.168.43.251:50070'>
<button type='submit'>WebGUI of Namenode</button>
</form>
""")

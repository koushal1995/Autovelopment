#!/usr/bin/python36

print("content-type: text/html")
print("")

import cgi
import subprocess as sp

form = cgi.FieldStorage()
ips = form.getvalue('dn1')
#ips = form.getvalue('ips')

#ips = ips.split(",")
print(ips)

#for i in ips:
#setup_datanodes = sp.getstatusoutput('sudo ansible-playbook /root/Ansible_playbooks/installation_hadoop.yml')
#print(setup_datanodes)
start_datanodes = sp.getstatusoutput("sudo ansible-playbook /root/Ansible_playbooks/datanode.yml --extra-vars='ip=192.168.43.251'")
print(start_datanodes)
if start_datanodes[0] ==0:
	print("datanodes succesfully started...")
	print("""
		<form action='upload.py'>
			<table align='center'>
				<tr><td><a href='http://192.168.43.251:50070'>Click here to get WebGUI of Datanode</a></td></tr>
				<tr><td>Upload Files<input type='text' name='fileaddr' placeholder='enter the location of file' /><td><input type='submit' /></td></tr>
			</table>
		</form>
		""")
else:
	print("starting datanodes failed.")
	exit()

#!/usr/bin/python36

print("content-type: text/html")
print("")

import cgi
import subprocess as sp

print("""
<form action='start_name_node.py' method='get' na>
	<table align='center' margin='top'>
		<tr>
			<td>Select a Namenode</td>
			<td><select name='namenode'>
				<option>192.168.43.108</option>
				<option>192.168.43.110</option>
			    </select>
			</td>
			<td><input type='submit' placeholder='Start Namenode'>
			</td>
	</table>
</form>
""")

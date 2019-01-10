#!/usr/bin/python36

print("content-type: text/html")
print("")

print("""
<form action='start_datanodes.py'>
	<table align='center' margin-top='100px' >
		<tr>
			<td>Select the IPs of datanodes</td>
			<td><input type='checkbox' name='dn1' value='192.168.43.185'>192.168.43.185</td>
			<td><input type='checkbox' name='dn2'>192.168.43.222</td>
			<td><input type='submit' />
		</tr>
		<!--<tr>
			<td>Enter the IPs</td>
			<td><input type='text' name='ips' /></td>
			<td><button type='submit'>Start datanodes</button></td>
		</tr>-->
	</table>
</form>
""")

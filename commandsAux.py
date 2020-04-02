
{
#Template for cisco 2911 router commands  sequence 
"Router_device_name":["import paramiko","ssh=paramiko.SSHClient()","ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())",
			  "ssh.connect('ip_address_device',ssh_port, 'device_user', 'device_password')","chan = ssh.invoke_shell()","chan.send('copy running-config  tftp:\\n')",
			  "chan.send('tftp_address\\n')","chan.send('ip_address_device\\n')","time.sleep(3)"],

#Template for 3com 4800g Switch commands  sequence 
"Switch_device_name":["import paramiko","ssh=paramiko.SSHClient()","ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())",
		  "ssh.connect('ip_address_device',ssh_port, 'device_user', 'device_password')","chan = ssh.invoke_shell()",
		  "chan.send('backup startup-configuration to tftp_address ip_address_device.cfg\\n')","time.sleep(1)"],

#Template for dell powerconnect 6224  Switch commands  sequence 
"Switch_device_name":["import time","import telnetlib","telnet=telnetlib.Telnet('ip_address_device')",'telnet.write("device_user".encode("ascii") + b"\\r")',
			"telnet.write('device_password'.encode('ascii') + b'\\r')","telnet.write('enable'.encode('ascii') + b'\\r')",
			"telnet.write('copy startup-config tftp://tftp_address/dist-cc.cfg'.encode('ascii') + b'\\r')",
			"telnet.write('y'.encode('ascii') + b'\\r')","time.sleep(10)","telnet.close()"],

#Template for 3com 4200G Switch commands  sequence 
"Switch_device_name":["import paramiko","ssh=paramiko.SSHClient()","ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())",
		  "ssh.connect('ip_address_device',ssh_port, 'device_user', 'device_password')","chan = ssh.invoke_shell()","chan.send('\\n')",
		  "chan.send('tftp tftp_address put 3comoscfg.cfg ip_address_device.cfg\\n')","time.sleep(1)","ssh.close()"],

#Template for HP 1920-24G Switch commands  sequence 
"Switch_device_name":["url = 'http://ip_address_device/iss/ati_index.html'",
		  "values = {'Gambit':'','Login' : 'device_user','Password' : 'device_password','submit':'Sign in'}",
		  "data = urllib.urlencode(values)",
		  "full_url= url + '?' + data",
		  "response = urllib2.urlopen(full_url)",
		  "soup = BeautifulSoup(response)",
		  "url='http://ip_address_device/iss/config.bin?Gambit='+(soup.find('frame', {'name': 'front'}).get('src')).split('=',)[1]+'&dumy'",
		  "response = urllib2.urlopen(url)",  
		  "serverfarm2 = open(repositorio+'\ip_address_device.bin', 'w')",
		  "serverfarm2.write(response.read())",
		  "serverfarm2.close()"],

#Template for 3com 2226 Switch commands  sequence 
"Switch_device_name": ["from cookielib import CookieJar","cj = CookieJar()","opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))",
		  "url = 'http://ip_address_device/cgi/login.cgi'","values = {'Username' : 'device_user','Password' : 'device_password'}",
		  "data = urllib.urlencode(values)","response = opener.open(url, data)","url = 'http://ip_address_device/wbackup.dat'",
		  "response = opener.open(url, data)", 		  
		  "archivo = open(repositorio+'\ip_address_device.wss','w')","archivo.write(response.read())","archivo.close()"],	

#Template for 3com 4210 Switch commands  sequence 
"Switch_device_name": ["from cookielib import CookieJar","cj = CookieJar()","opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))",
		  "url = 'http://ip_address_device/cgi/login.cgi'","values = {'Username' : 'device_user','Password' : 'device_password'}",
		  "data = urllib.urlencode(values)","response = opener.open(url, data)","url = 'http://ip_address_device/wbackup.dat'",
		  "response = opener.open(url, data)", 	  
		  "archivo = open(repositorio+'\ip_address_device.wss','w')","archivo.write(response.read())","archivo.close()"],			
		  
#Template for 3com superstack 4200 Switch commands  sequence 
"Switch_device_name":["from cookielib import CookieJar","cj = CookieJar()","opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))",
		  "url = 'http://ip_address_device/cgi/login.cgi'","values = {'Username' : 'device_user','Password' : 'device_password'}",
		  "data = urllib.urlencode(values)","response = opener.open(url, data)","url = 'http://ip_address_device/wbackup.dat'",
		  "response = opener.open(url, data)", 		  
		  "archivo = open(repositorio+'\ip_address_device.wss','w')","archivo.write(response.read())","archivo.close()"],


#Template for Allied Telesis AT-GS950/24  Switch commands  sequence 
"Switch_device_name":["url = 'http://ip_address_device/'",
				 "p = urllib2.HTTPPasswordMgrWithDefaultRealm()",
				 "p.add_password(None, url, 'device_user', 'device_password')",
				 "handler = urllib2.HTTPBasicAuthHandler(p)",
				 "opener = urllib2.build_opener(handler)",
				 "urllib2.install_opener(opener)",
				 "urllib2.urlopen(url)",
				 "url='http://ip_address_device/dev01/bin/bup_backup_p.rhtm?ServerAdd=tftp_address&FileName=ip_address_device.cfg&UserNote='",
				 "response=urllib2.urlopen(url)",
				 "time.sleep(20)"],

#Template for 3com  4210 Switch commands  sequence 
	"Switch_device_name":["url = 'http://ip_address_device/'",
				 "p = urllib2.HTTPPasswordMgrWithDefaultRealm()",
				 "p.add_password(None, url, 'device_user', 'device_password')",
				 "handler = urllib2.HTTPBasicAuthHandler(p)",
				 "opener = urllib2.build_opener(handler)",
				 "urllib2.install_opener(opener)",
				 "urllib2.urlopen(url)",
				 "url='http://ip_address_device/dev01/bin/bup_backup_p.rhtm?ServerAdd=tftp_address&FileName=ip_address_device.cfg&UserNote='",
				 "response=urllib2.urlopen(url)",
				 "time.sleep(20)"],	 

#Template for 3com  3812 Switch commands  sequence 
   "Switch_device_name":["url = 'http://ip_address_device/'",
				 "p = urllib2.HTTPPasswordMgrWithDefaultRealm()",
				 "p.add_password(None, url, 'device_user', 'device_password')",
				 "handler = urllib2.HTTPBasicAuthHandler(p)",
				 "opener = urllib2.build_opener(handler)",
				 "urllib2.install_opener(opener)",
				 "urllib2.urlopen(url)",
				 "url='http://ip_address_device/config/save_config.htm'",
				 "values={'page':'backupConfig','tftpCfgToServerIpAddress':'tftp_address','cfgToServerDestFile':'ip_address_device.cfg'}",
				 "data = urllib.urlencode(values)",
				 "req=urllib2.Request(url, data)",
				 "response=urllib2.urlopen(req)",
				 "time.sleep(20)"],

#Template for 3com  5500-SI 28-Port  Switch commands  sequence 
"Switch_device_name":["import paramiko","ssh=paramiko.SSHClient()","ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())",
			  "ssh.connect('ip_address_device',ssh_port, 'device_user', 'device_password')","chan = ssh.invoke_shell()","chan.send('\\n')",
			  "chan.send('tftp tftp_address put unit1>flash:/3comoscfg.cfg ip_address_device.cfg\\n')",  
			  "chan.send('quit\\n')","time.sleep(2)"],

#Template for 3com  3226 Switch commands  sequence 
"Switch_device_name":["import paramiko","ssh=paramiko.SSHClient()","ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())",
			  "ssh.connect('ip_address_device',ssh_port, 'device_user', 'device_password')","chan = ssh.invoke_shell()","chan.send('\\n')",
			  "chan.send('tftp tftp_address put unit1>flash:/3comoscfg.cfg ip_address_device.cfg\\n')",  
			  "chan.send('quit\\n')","time.sleep(2)"],
			  

#Template for DD-WRT wlan firmware commands  sequence 
"Access_point_device_name":["url = 'http://ip_address_device/'",
			"p = urllib2.HTTPPasswordMgrWithDefaultRealm()",
			"p.add_password(None, url, 'device_user', 'device_password')",
			"handler = urllib2.HTTPBasicAuthHandler(p)",
			"opener = urllib2.build_opener(handler)",
			"urllib2.install_opener(opener)",
			"urllib2.urlopen(url)",
			"url = 'http://ip_address_device/nvrambak.bin'",
			"response=urllib2.urlopen(url)",			
			"archivo = open(repositorio+'\ip_address_device.bin','w')",
			"archivo.write(response.read())",
			"archivo.close()"],

#Template for DD-WRT wlan firmware commands  sequence 
"Access_point_device_name":["import paramiko",
				"import time",
				"ssh=paramiko.SSHClient()",
				"ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())",
				"ssh.connect('ip_address_device',ssh_port, 'device_user', 'device_password')",				
				"scp = SCPClient(ssh.get_transport())",
				"scp.get('/tmp/running.cfg',repositorio + '\ip_address_device.cfg')",
				"ssh.close()",
				"time.sleep(5)"],
							
}
	   

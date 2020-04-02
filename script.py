import subprocess
import os
import sys

#Library for scrapping
import urllib
import urllib2
from prettytable import PrettyTable
import shutil
import paramiko
from bs4 import BeautifulSoup


import logging
import logging.handlers

#Library for create folders with name date
import time
import datetime
import calendar

import smtplib
from email.mime.text import MIMEText
from scp import SCPClient

#Email Constants
SMTP_HOST = SMTP_ADRRESS  #Write the variable between""
LOG_FILE = "C:\script.Dispositivos.Backup\log\script.log"

#List destination address separated with commas
EMAILS  = [DESTINATION_ADDRESS_MAIL]

# Send Notification Email		
def send_email(msgbody, subject, emails):

	print("\tSending Email Notification...\n")
	
	toaddrs = emails
	fromaddr = SOURCE_ADDRESS_MAIL

	# Add the From: and To: headers at the start!
	msg_headers = "From: Script Backup Network <renovacion-noreply@domain>\r\n"
	msg_headers = msg_headers + "Subject: " + subject + "\r\n"
	sendmsg = msg_headers + msgbody

	server = smtplib.SMTP(SMTP_HOST)
	server.set_debuglevel(0)
	server.sendmail(fromaddr, toaddrs, sendmsg)
	server.quit()


def init_logger():
	global logger

	# create logger
	logger = logging.getLogger(__name__)

	# create file handler
	print("Creating handler...")
	fh = logging.FileHandler(LOG_FILE)
	#fh = logging.StreamHandler(LOG_FILE)

	# create formatter
	print("Creating formatter...")
	formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')

	# add formatter to fh
	print("Adding formatter to handler...")
	fh.setFormatter(formatter)

	# add fh to logger
	print("Adding handler to logger...")
	logger.addHandler(fh)	
	
	logger.setLevel('INFO')

if __name__ == "__main__":

													   ###################################
									         	  ######## Creating path repositorio #############				
													   ####################################

	init_logger()

	logger.info("Starting the script....")

	#Folder reation for config file storage
	now = datetime.datetime.now()
	router = "C:\script.Dispositivos.Backup\{0}\{1}-{2}\{3}-{4}.(PARCIAL)\Router\\".format(str(now.year),str(now.month),str(calendar.month_name[now.month]),str(now.day),now.strftime("%A"))
	switch = "C:\script.Dispositivos.Backup\{0}\{1}-{2}\{3}-{4}.(PARCIAL)\switch\\".format(str(now.year),str(now.month),str(calendar.month_name[now.month]),str(now.day),now.strftime("%A"))
	wireless = "C:\script.Dispositivos.Backup\{0}\{1}-{2}\{3}-{4}.(PARCIAL)\wireless\\".format(str(now.year),str(now.month),str(calendar.month_name[now.month]),str(now.day),now.strftime("%A"))

	#Base folder
	repositorio= "C:\script.Dispositivos.Backup\{0}\{1}-{2}\{3}-{4}.(PARCIAL)\\".format(str(now.year),str(now.month),str(calendar.month_name[now.month]),str(now.day),now.strftime("%A"))

																				
															#####################################		 
													    ######## Creating folder repositorio #########
															#####################################

	
	logger.info("Creating folders....")
	os.makedirs(router)
	os.makedirs(switch)	
	os.makedirs(wireless)
	

	#Read  collect  of auxiliary commands
	with open('commandsAux.py' ,'r') as f:
		commands= eval(f.read())
	f.close()
		
																#####################		 
															########  Open TFTP  #########
																#####################	

	logger.info("Opening TFTP")
	#Open  tftp configuration folder 												
	config = open(r"C:\Program Files\Tftpd64\tftpd32.ini","r+") 
	config.seek(52,0)
	#configura tftp con el path de la carpeta  router como destino
	config.write(repositorio +"\n")  
	config.close()
	time.sleep(2)
	#abrir aplicacion tftp
	tftp=subprocess.Popen(r"C:\Program Files\tftpd64\tftpd64.exe") 

																##############################################		 
															########  First attemp of download config file #########
																##############################################	
	print ("Starting download fist attemp" )													
														
	for device in commands:
		try:
			logger.info("Downloading file from:" + str(device))
			print (device)
			for c in commands[device]:
				exec (c)
			time.sleep(4)
		except urllib2.URLError as e:
			logger.info(str(e))
			print (str(e))
			
		except os.error as e:
			logger.info(str(e))
			print ("One error have found: " + str(e))
			logger.warning(str(e))
			
		except paramiko.ssh_exception.AuthenticationException:
			logger.info(str(e))
			print ("Failed the authentication please reviews the credentials : %s")
			
		except paramiko.SSHException as sshException:
			print  ("Coudn't be estabilsh ssn connection : %s" % sshException)
			logger.warning(sshException)
			


																##############################################		 
															########  Second attemp of download config file   #########
																##############################################	

	print ("\n"+"Starting Second attemp................"+"\n")
	logger.info("Starting Second attemp" )
											
	######## Numbering the  devices
	nro_device = 0 
	downloaded_device = 0

	t = PrettyTable(["Devices", "Downloaded","Total","Error Message"])
	t.align["devices "] = "l" 
	t.align["Downloaded"] = "c" 
	t.align["Total"] = "l" 
	t.align["Error Message"] = "l" 


	for device in commands:
			try:
				if os.path.isfile(repositorio + "\\" + device) or os.path.isfile(repositorio + "\\" +device+".bin") or  os.path.isfile(repositorio + "\\" +device +".cfg") or os.path.isfile(repositorio +  "\\" +device +".wss"):
					downloaded_device += 1
					t.add_row([format(nro_device)+"-"+ device+"&%$#","downloaded",format(downloaded_device),""])
				else:
					try:
						nro_device += 1	
						print(device)													
						logger.info("Downloading file from:" + str(device) + "second attemp" )
						for c in commands[device]:
							exec (c)
						time.sleep(4)
						if os.path.isfile(repositorio + "\\" + device) or os.path.isfile(repositorio + "\\" +device+".bin") or  os.path.isfile(repositorio + "\\" +device +".cfg") or os.path.isfile(repositorio +  "\\" +device +".wss"):
								downloaded_device += 1
								t.add_row([format(nro_device)+"-"+ device,"downloaded",format(downloaded_device),""])
						else:
								t.add_row([format(nro_device)+"-"+ device,"Download Failed",format(downloaded_device)],"")
					except urllib2.URLError as e:
						logger.info(str(e))
						t.add_row([format(nro_device)+"-"+ device,"Download Failed",format(downloaded_device),"Re Log"])
						print (e)
						
					except:
						t.add_row([format(nro_device)+"-"+ device,"Download Failed",format(downloaded_device),sys.exc_info()[0]])
						logger.info(str(e))
						print("Unexpected error:", sys.exc_info()[0])
						
			except:															
				print("Unexpected error:", sys.exc_info()[0])
				logger.info("Unexpected error:" + str(e))
				
											

											
															  	######################		 
															########  Closing Tftp #########
																#######################
	tftp.terminate()	

	print ("closing TFTP..........."+"\n")
	logger.info("Closing TFTP" )

	### Saving the table on file		
	with open("downloadeds.txt", "w") as registro:
		registro.write(format(t))
		registro.write("\n "+"Destination folder:  "+"\n")
		registro.write(router +"\n")
		registro.write(switch +"\n")
		registro.write(wireless+"\n")
		registro.close()
			
														####################################################		 
													#########  Moving downloaded files to respect folder ########
														####################################################

	print("MOving files to respect folder........")													
	logger.info("MOving files to respect folder" )
	for filename in os.listdir(repositorio):
		if filename[0] == 'R': 
			shutil.move(repositorio + "\\" + filename,router)	
		elif filename[0] == 'd' or filename[0] == 's':
			shutil.move(repositorio + "\\" +filename,switch)
		elif filename[0] == '2' or filename[0] == 'w':
			shutil.move(repositorio + "\\" +filename,wireless)		

														######################################		 
													#########    Notification by email   ########
														######################################

	print ("Sending Mail Notification......."+"\n")
	logger.info("Sending Email")

	# Open a plain text file for reading.  For this example, assume that
	# the text file contains only ASCII characters.
	fp = open("downloadeds.txt", 'rb')
	# Create a text/plain message
	msg = MIMEText(fp.read())
	fp.close()

	send_email(msg.as_string(), "Network Backup Notification: " + time.strftime("[%d %b %Y]", time.localtime()) , EMAILS)         
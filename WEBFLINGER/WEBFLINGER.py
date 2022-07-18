#！/usr/bin python

## Eyecandy: rich and textual (need to add rich to an install list)



########################################
## SLAP imports (exploits, main, etc
########################################
import main # this file holds the sys append so it knows where to look
import bedb
import utility 

########################################
## SYS/python imports
########################################
import os
import sys
import subprocess as sp
import readline
import random
#import glob
import signal
import sys
import multiprocessing
import time

import requests 
from requests.structures import CaseInsensitiveDict

########################################
## Eyecandy (rich) imports
########################################
from rich.console import Console
from rich.table import Table
from rich import print
console = Console()


########################################
## Utility
########################################

## CTRL c graceful exit (closes notification socket properly)
def signal_handler(signal, frame):
	print('\nExiting gracefully...\n')
	sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

## RootCheck
if os.getuid() != 0:
        exit("\nYou need root to run this program!")


## -- Defining Vars -- ##
DB_name = "webflinger_db" ## new names: webflinger_db
TABLE_name = "webflinger_host_table" #webflinger_host_table

########################################
## Startup
########################################

utility.notif('','WEBFLINGER started','appname')

## color gen
rand_color = utility.random_color

#Pulling target IP from user input so everything can access it (should be done by scan_and_dump, but this is a fallback)
#DB_targetIP = bedb.loadCONFIG.ip_addr

########################################
## Menu
########################################

### green3 looks really cool here - set as default?

def menu():
	os.system('clear')
	print(r"""[bold """ + rand_color + """]
  _      _________    ______   _____  ______________ 
 | | /| / / __/ _ )  / __/ /  /  _/ |/ / ___/ __/ _ \ 
 | |/ |/ / _// _  | / _// /___/ //    / (_ / _// , _/
 |__/|__/___/____/ /_/ /____/___/_/|_/\___/___/_/|_|                                              
        
        by ryanq47       
       [/bold """ + rand_color + """] """)



## --- Menu --- ###
	print(r""" [bold underline]
OPTIONS[/bold underline] 

a) Fuzz (random things on end of url?)
b) 
c)



Type in IP address to view info, or set options: """)
	#statement = input("").lower()
menu()


#----------------------------------------------------------------------------------------------------
## This scans and writes to DB
#--------------------------------------------------------------------------------------------------########################################
## Main Request section
########################################


def fuzzer():
	## -- Variables -- ##
	bedb.loadCONFIG('config','webflinger_config','config.json', 'GUIoff') ## loading file
	FILE_LIST = bedb.loadCONFIG.attack_type
    
    	## -- params n stuff for request -- ##
    	
	headers = CaseInsensitiveDict()
    
	headers = {
	"X-Requested-With" : "testheader"
	}    

	params = {
	#'output_format': 'json_extended',
	'test':'test',
	}
    
    
	bedb.loadCONFIG('config','webflinger_config','config.json', 'GUIoff')
	base_url = "http://" + bedb.loadCONFIG.ip_addr + "/" #"http://10.73.180.233/"
	print(base_url)
    
    
    ####################
    # Main Loop
    ####################
	f = open("webflinger_data/webflinger_logs/" + bedb.loadCONFIG.ip_addr + ".log", "w")
    	
	with open("webflinger_data/webflinger_modules/webflinger_lists/" + FILE_LIST, "r") as inject:
		for line in inject:
			stripped_line = line.strip()
		    
			   ## -- variables -- ##
			url = base_url + stripped_line
			print(url) #<< -- this looks really cool
			    
			## -- main request -- ##

			response = requests.get(url, headers=headers, params=params)

			status_response = response
			full_response = response.text
			## logging here, maybe add this into utility somewhere for standardization
			f.write("\n== " + utility.timestamp + " ==============================================\n" + str(response) + "\n- - - - - - - - - - \n" +  response.text + "\n")
			
			## -- logic -- ##
			os.system('clear')
			if "The requested URL was not found on this server" in response.text:
				print('No valid pages found: ' + str(response))
				pass
				print("====================")
			elif "200" in response:
				print("Found successful URL/URI! Waiting for user input to continue")
				input()
			else:
				
				print("Response: " + full_response, status_response)

				print("====================")
				
				#os.system('clear')
			## -- Delay -- ##
			if bedb.loadCONFIG.delay == "0":
				delay_placeholder = "pass"
				
			if bedb.loadCONFIG.delay == "random":
				random_delay = random.randrange(1,50)
				print("Waiting for " + str(random_delay) + " seconds till next request...")
				delay_placeholder = time.sleep(random_delay)
			else:
				print("Waiting for " + bedb.loadCONFIG.delay + " seconds till next request")
				delay_placeholder = time.sleep(int(bedb.loadCONFIG.delay))
				
			delay_placeholder
		input('Attack Completed, hit enter to go to menu')

	f.close()
#----------------------------------------------------------------------------------------------------
## ALl of this below pulls FROM db
#----------------------------------------------------------------------------------------------------

########################################
## Variable load + attack
########################################

bedb.loadCONFIG('config','webflinger_config','config.json', 'GUIoff') ## loading file
FILE_LIST = bedb.loadCONFIG.attack_type



#def variable_load():
	########################################
	## Loading attack type from config
	########################################
	#bedb.loadCONFIG('config','webflinger_config','config.json', 'GUIoff') ## loading file
	#variable_load.attack_config = bedb.loadCONFIG.attack_type ## loading variable
	#print(variable_load.attack_config)



	########################################
	## Loading Varibles from menu/config
	########################################


	########################################
	## Loading attacklist from DB
	########################################
	
	#bedb.loadCOLUMN(DB_name,TABLE_name, DB_targetIP, 'open_ports') # loading file
	#variable_load.DB_attackList = bedb.loadCOLUMN.key_data 
	#print(variable_load.DB_attackList)

########################################
## Attack groupings
########################################


#FILE_LIST = #"path_traversal.txt"
	


########################################
## Options Menu
#########################################	

def show_options():
	print(" ---------------------------------------- ")
	bedb.loadCONFIG('config','webflinger_config','config.json', 'GUIon')


def set_options():
	clear()
	bedb.loadCONFIG('config','webflinger_config','config.json','GUIon')	
	
	OPTION_CHANGE = option_arg #(located in logic section)
		
	OPTION_VALUE = input("Enter value of " + OPTION_CHANGE + ": ")

	bedb.writeCONFIG('config','webflinger_config','config.json', OPTION_CHANGE, OPTION_VALUE)
	

	
	clear() #clears tomake room for new graph
	bedb.loadCONFIG('config','webflinger_config','config.json','GUIon')	# reloads graphs to see

########################################
#DB Host lookup
########################################
def db_ip_lookup(targetIP):
	try:
		#ping_load()
		print('Loading ' + targetIP + '... this may take a second')
		#gui_tmp()
	except:
		print('placeholder')

########################################
## Clear + jump to menu function
#######################################
	
def clear():
	os.system('clear')
	menu()
	

########################################
## Program Logic
########################################

statement = input("").lower()

while True:
	########################################
	## Attack Type config 
	########################################
	if statement == 'a':
		#variable_load()
		fuzzer()
	if statement == 'b':
		pass

		
	########################################
	## Additional Utilities
	########################################		
	if '.' in statement:
		db_ip_lookup(statement)
	if 'menu' in statement:
		menu()
	if statement == 'menu':
		menu()
	if statement == 'clear':
		clear()
	if statement == 'slap':
		utility.slap_img()
	if statement == 'slap fail':
		utility.slap_fail_img()
	if statement == 'test':
		ping_load()
	########################################
	## Options/Menu
	########################################		
	if 'set options' in statement:
		option_arg = statement[12:50]
		set_options()
		
	if statement == 'show options':
		show_options()
		
	########################################
	## Moving around
	########################################
	elif statement=="h":
		print("""\nHelp
			""")
	elif statement == "exit":
		slap_exit()
	elif statement == "quit":
		slap_exit()

	else:
		menu()
	statement = input("").lower()



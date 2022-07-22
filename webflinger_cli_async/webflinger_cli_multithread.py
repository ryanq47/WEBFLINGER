
######################
## General imports
######################
import random, time, multiprocessing
import os
import utility
import multiprocessing
import requests
from requests.sessions import Session
import sys


######################
## Asyncio imports
######################
from aiohttp.resolver import AsyncResolver
import asyncio
import aiohttp
from aiohttp.client import ClientSession


######################
## Arg Parse Imports
######################
import argparse
'''
wfuzz: lost by a few seconds :(


NOTES:
The for loop is the limiting factor here, need to find a way to put in multiple values without the loop, as the loop has to run everything under it OR find a way to pipe the loops results out,thus only looping the loop. ONce that it figured out, async should run SUPER fast
		Side note, it may even be faster to generate URLs instead of using a list, then piping that into 	 			 	async if it really is that fast


Async doc: docs.aiohttp.org/en/stable


'''
utility.banner()
print(" -- A LOCAL directory Bruteforcer (still can't hold a candle to wfuzz on external searches) -- \n")
######################
## Arg Parse def
######################
ap = argparse.ArgumentParser()

## -- setting flags -- ##
ap.add_argument("-w", "--wordlist", required=True,
	help="Wordlist for bruteforce")
	
ap.add_argument("-ip", "--ip_address", required=True,
	help="IP address")	
	
ap.add_argument("-e", "--engine", 
	help="To run with ASYNCIO (async) or SessionRequests (sess) (Both are limited by a for loop currently, or the webserver internet speed. asyncio runs slightly faster rn")
		
## -- something so it can be read -- ##
args = vars(ap.parse_args())



## -- Setting variables -- ##
WORDLIST = (args["wordlist"])
IP = (args["ip_address"])

######################
## Stats
######################

def STATS():
	print("End of list")
	toc = time.perf_counter()
	print(f"Ran in {toc - tic:0.4f} seconds")
	
######################
## External Loop - maybe use pycurl for this
######################
## session is faster than requests by a decent amount
	 
def main():
	f = open("attack_external.py","w")
	
	f.write('''
import requests
from requests.sessions import Session
s = requests.Session()''')
	
	with open(WORDLIST, "r") as inject:
		for line in inject:
			url = 'http://' + IP + '/' + line.rstrip("\n")
			## request ##
			f.write('''
response = s.get("''' + url + '''")
			
## logic ##
if '404' in response.text: 
	pass

else:
	print("[+]" + str(response) + "''' + url + '''")
				''')

######################
## LOCAL loop
######################

	

def async_main():
	print("^Ignore the event loop error plz and thanks^")
	
	## Config here is for future implementation
	'''######################
	## Config
	######################	

	headers = {
		'content-type':'GIF/Image'
		}	
	## -- cache settings -- ##
	conn = aiohttp.TCPConnector(ttl_dns_cache=100)
	
	##-- DNS server to use -- ##
	resolver = AsyncResolver(nameservers=["1.1.1.1", "8.8.8.8"])
	conn = aiohttp.TCPConnector(resolver=resolver)
	######################
	## Loading in urls
	######################'''
	
	f = open('internal_attack.py','w')
## imports
	f.write('''
######################
## Asyncio imports
######################
from aiohttp.resolver import AsyncResolver
import asyncio
import aiohttp
from aiohttp.client import ClientSession
''')
	
	f.write('''async def async_main():
	async with aiohttp.ClientSession() as session:''')
	## for loop
	with open(WORDLIST, "r") as inject:
		for line in inject:
			url = 'http://'+ IP +'/' + line.rstrip("\n")
			
			## Writing Asyncio Logic ##
			f.write('''
		#try:
		async with session.get("''' + url + '''") as response:
			if '404' in str(response.status):
				pass
			else:
				print("[+] Response:", str(response.status) + " : " + "''' + url + '''")
		#except:
			#print("Error with URL ''' + url + ''' ... Skipping")
			''')			#html = await response.text()
	## end logic + loop starter
	f.write('''
	print("Done :) ")
loop = asyncio.get_event_loop()
loop.run_until_complete(async_main())
	''')


tic = time.perf_counter()		

async_main()
exec(open('internal_attack.py').read())

######################
## which engine to run
######################
#ENGINE = (args["engine"])
#if ENGINE == 'sess':
	#main()
#else:
	#loop = asyncio.get_event_loop()
	#loop.run_until_complete(async_main())

#main()	
STATS()


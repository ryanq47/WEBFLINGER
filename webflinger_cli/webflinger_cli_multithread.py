import random, time, multiprocessing
import os
import utility
import multiprocessing
import requests
from requests.sessions import Session
import sys
import asyncio
import aiohttp
from aiohttp.client import ClientSession

import argparse
'''
wfuzz: lost by a few seconds :(


NOTES:
The for loop is the limiting factor here, need to find a way to put in multiple values without the loop, as the loop has to run everything under it OR find a way to pipe the loops results out,thus only looping the loop. ONce that it figured out, async should run SUPER fast
		Side note, it may even be faster to generate URLs instead of using a list, then piping that into 	 			 	async if it really is that fast


Async doc: docs.aio.http.org/en/stable


'''
utility.banner()
print(" -- A directory Bruteforcer and Response coercion tool -- \n")
######################
## Arg Parse def
######################
ap = argparse.ArgumentParser()
ap.add_argument("-w", "--wordlist", required=True,
	help="Wordlist for bruteforce")
ap.add_argument("-ip", "--ip_address", required=True,
	help="IP address")	
	
ap.add_argument("-e", "--engine", 
	help="To run with ASYNCIO (async) or SessionRequests (sess) (Both are limited by a for loop currently, or the webserver internet speed. asyncio runs slightly faster rn")

args = vars(ap.parse_args())




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
## Main Session Loop
######################
s = requests.Session()
## session is faster than requests by a decent amount
	 
def main():
	with open(WORDLIST, "r") as inject:
		for line in inject:
			url = 'http://' + IP + '/' + line.rstrip("\n")
			## request ##
			response = s.get(url)
			
			## logic ##
			if '404' in response.text: 
				pass

			else:
				print("[+]" + str(response) + url)

######################
## Main Asyncio Loop
######################
async def async_main():
	print("^Ignore the event loop error plz and thanks^")
	with open(WORDLIST, "r") as inject:
		for line in inject:
			url = 'http://'+ IP +'/' + line.rstrip("\n")
			
			async with aiohttp.ClientSession() as session:
				async with session.get(url) as response:
					if '404' in str(response.status):
						pass
					else:

						print("[+] Response:", str(response.status) + " : " + url)
					
							#print("Content-type:", response.headers['content-type'])

							#html = await response.text()
							#print("Body:", html[:15], "...")
		print('done')


tic = time.perf_counter()		

######################
## which engine to run
######################
ENGINE = (args["engine"])
if ENGINE == 'sess':
	main()
else:
	loop = asyncio.get_event_loop()
	loop.run_until_complete(async_main())

	
STATS()


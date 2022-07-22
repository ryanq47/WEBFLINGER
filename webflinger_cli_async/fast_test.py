import aiohttp
import asyncio

import time

def STATS():
	print("End of list")
	toc = time.perf_counter()
	print(f"Ran in {toc - tic:0.4f} seconds")
'''
async def main():
	with open("path_traversal", "r") as inject:
		for line in inject:
			url = 'http://127.0.0.1/' + line.rstrip("\n")
				
			async with aiohttp.ClientSession() as session:
				async with session.get(url) as response:
					print(url)
					print("Status:", response.status)
					#print("Content-type:", response.headers['content-type'])

					#html = await response.text()
					#print("Body:", html[:15], "...")
		print("Done")
'''




#z = ['test','test2','test3','test','test2','test3','test2','test3','test','test2','test3',]*100

#f = open('path_traversal', "r")

#def test():
	#return next(print('http://127.0.0.1/' + i) for i in z)

	
async def main():
	with open('path_traversal', "r") as inject:
		for line in inject:
			url = 'http://127.0.0.1/' + line.rstrip("\n")
			
			async with aiohttp.ClientSession() as session:
				async with session.get(url) as response:
					if '404' in str(response.status):
						pass
					else:
						print(url)
						print("Status:", response.status)
					
							#print("Content-type:", response.headers['content-type'])

							#html = await response.text()
							#print("Body:", html[:15], "...")
		print('done')



tic = time.perf_counter()
loop = asyncio.get_event_loop()
#test()
loop.run_until_complete(main())
STATS()

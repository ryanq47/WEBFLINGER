import asyncio
import aiohttp
from aiohttp.client import ClientSession

async def main():
	async with aiohttp.ClientSession() as session:
		async with session.get('http://127.0.0.1') as response:
			if '404' in str(response.status):
				pass
			else:

				print("[+] Response:", str(response.status) + " : ")
				
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
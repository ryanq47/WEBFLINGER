import pyfiglet
import time

def banner():
	banner = pyfiglet.figlet_format("webflinger")
	print(banner) 
	
def timerstart():
	timerstart.start = time.perf_counter()


def timerstop():
	stop = time.perf_counter()
	totaltime = timerstart.start - stop
	print("Downloaded the tutorial in " + totaltime + " seconds")




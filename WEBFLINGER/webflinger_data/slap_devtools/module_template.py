import pyfiglet
import subprocess as sp

import main
import bedb

from rich import print

def main():
	pass

########################################
## Color/Global Variables
########################################

color = "[blue]"
fail_color = "[red bold]"
title_color = "[bold blue]"

bedb.loadCONFIG('config','slap_config','config.json', 'GUIoff')
########################################
## Main Exploit
########################################

def exploit(targetIP, hostname):

	ascii_banner = pyfiglet.figlet_format("Exploit: EXPLOIT NAME")
	print(title_color + ascii_banner)
	
	result = sp.getoutput("python3 EXPLOIT" + variables_needed)
	
	if "ERROR MESSAGE THAT FITS ERROR RESPONSE" in result:
		print(fail_color + "!! - ERROR MESSAGE HERE- !!")
		
		
def checker():
	pass
	
	
#test	
#exploit(variables_needed)

if __name__ == "__main__":
	main()

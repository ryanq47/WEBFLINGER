########################################
## Pyhton/Sys imports
########################################
import os
import json
########################################
## SLAP imports
########################################
import utility
########################################
## Eyecandy/rich imports
########################################
from rich.console import Console
from rich.table import Table

########################################
## Utility
########################################
rand_color = utility.random_color


## Testing --
## to the DB file
########################################
## For testing, not sure if needed. Keep for now
########################################
ipaddr = '192.168.1.1'
ports = ['1','22','443']
services = ['ICMP','SSH','HTTPS']




########################################
## Global Variables
########################################

DB_name = "hackbox_db" ## Best to put application name here or if in hackbox, keep it hackbox_db)
TABLE_name = "hackbox_ip_table"

data = {

            'ip_addr' : ipaddr,
            'open_ports' : ports,
            'services' : services
}

def main():
	pass


########################################
## Unused but Create + del db
########################################
def CreateDB(DB_name):
        try:
            os.mkdir("Database/" + DB_name) #0o777)
            ## Note, if using outside of hackbox, create a folder called Database in the current working directory
        except:
            print('DB "' + DB_name + '" ready to go')
        ## 0o644 allows creator to  read + write, but everyone else to only read. maybe in future make option to choose diff levels of security (640, 600 etc)

        
def CreateTABLE(DB_name,TABLE_name):
        try:
            os.mkdir("Database/"+ DB_name + '/' + TABLE_name)
        except:
            print('Duplicate table detected, using previously created "' + TABLE_name + '"')


#----------------------------------------------------------------------------------------------------
## Backend
#----------------------------------------------------------------------------------------------------
		
########################################
## Write Column
########################################
            
def writeCOLUMN(DB_name,TABLE_name,FILE_name,KEY_contents): ## this is meant for writing an entire new json file/sturcutre
        with open("Database/" + DB_name + '/' + TABLE_name + '/' + FILE_name, 'w') as c:
            #print(c)
            jsondata = KEY_contents
            json.dump(jsondata, c)
            c.close()

        #Note this will overwrite existing file contents


	

########################################
## Read Column
########################################     
def readCOLUMN(DB_name,TABLE_name,FILE_name,KEY_value, name):
        r = open("Database/" + DB_name + '/' + TABLE_name + '/' + FILE_name, "r")
        json_str = (r.read())
        data = json.loads(json_str)
        readCOLUMN.key_data = (data[KEY_value])
        #print("--" + name + "--------------------------------------")
        #print(readCOLUMN.key_data)
        r.close()  
        
        ## Table stuff
        table = Table(title='')
        
        ##Column add
        table.add_column(name, style='green')
        
        ##Row add
        table.add_row(readCOLUMN.key_data)
        
        ## Final Part
        console = Console()
        console.print(table)
        
########################################
## Load Column
########################################        
def loadCOLUMN(DB_name,TABLE_name,FILE_name,KEY_name): ## the only difference between this and readCOLUMN is that this will load a value and not print it - handy for config files

	r = open("Database/" + DB_name + '/' + TABLE_name + '/' + FILE_name, "r")
	json_str = (r.read())
	data = json.loads(json_str)
	loadCOLUMN.key_data = (data[KEY_name])
	r.close()
	## Note!! to get value from here, use bedb.loadCOLUMN.key_data


def loadALL(DB_name,TABLE_name,FILE_name): ## this is good for loading all JSON, such as a config file
	with open("Database/" + DB_name + '/' + TABLE_name + '/' + FILE_name, "r") as file:
		key_data = json.load(file)
		
	print(key_data)
	file.close()
 
 
########################################
## SLAP config menu
########################################
#----------------------------------------------------------------------------------------------------
## Config
#----------------------------------------------------------------------------------------------------
		
def loadCONFIG(DB_name,TABLE_name,FILE_name, GUI): ## this could be much more efficent with maybe a for loop pulling each variaable
	# reading file with new value
	with open("Database/" + DB_name + '/' + TABLE_name + '/' + FILE_name, "r") as file:
		key_load_data = json.load(file)
		
	########################################
	## Loading config options
	########################################
	loadCONFIG.attack_type = key_load_data['attack_type']
	loadCONFIG.ip_addr = key_load_data['ip_addr']
	loadCONFIG.delay= key_load_data['delay']
	loadCONFIG.terminal_color = key_load_data['terminal_color']	


	########################################
	## Construting table
	########################################
	table_config = Table(title='Config')
        
	table_config.add_column("Option")
	table_config.add_column("Value")
	table_config.add_column("Possible Options")
	
        ########################################
	## Addomgrows
	########################################
	table_config.add_row("ip_addr:",loadCONFIG.ip_addr, "Target IP", style=rand_color)
	table_config.add_row("attack_type:",loadCONFIG.attack_type,"path_traversal, ETC", style=rand_color)
	table_config.add_row("delay:",loadCONFIG.delay,"delay between requests", style=rand_color)
	table_config.add_row("terminal_color:",loadCONFIG.terminal_color, "Color for SLAP - must reload to take affect",style=rand_color)                                                   

        
	########################################
	## GUI on/off
	########################################
	console = Console()
        ## Final Part
	if GUI == 'GUIoff':
		pass
	if GUI == 'GUIon':
		console.print(table_config)

def writeCONFIG(DB_name,TABLE_name,FILE_name, KEY_name, KEY_value): ## this is meant for changing a key
	

	########################################
	## Loading previous config files 
	########################################
	
	with open("Database/" + DB_name + '/' + TABLE_name + '/' + FILE_name, "r") as f:
		keys = json.load(f)
	savekey_attack_type = keys['attack_type']
	savekey_ip_addr = keys['ip_addr']
	savekey_delay = keys['delay']
	savekey_terminal_color = keys['terminal_color']


	########################################
	## Re-writing to file with changed options
	########################################	
	with open("Database/" + DB_name + '/' + TABLE_name + '/' + FILE_name, "w") as edit_out_file:

		wipe = {
			"ip_addr":savekey_ip_addr,
			"attack_type":savekey_attack_type,
			"delay":savekey_delay,
			"terminal_color":savekey_terminal_color,
			KEY_name:KEY_value ## This will overwrite any prevous value with the new value, and take the non #changed values and rewrite them
		}
		
		json.dump(wipe, edit_out_file)
		
	########################################
	## Reloading menu
	########################################
	loadCONFIG('config','webflinger_config','config.json', 'GUIon')


if __name__ == "__main__":
        main()

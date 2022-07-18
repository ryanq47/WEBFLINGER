## -- notifications
import json
from plyer.utils import platform
from plyer import notification
import random
import time
from rich import print
import os
import subprocess as sp

from datetime import datetime, date

########################################
## Time
########################################


now = datetime.now()
current_time = now.strftime("%H:%M:%S")
current_date = date.today()

timestamp = "Time: " + str(current_time) + " Date: " + str(current_date)
#timestamp()

########################################
## Notifications
########################################
def notif(notif_title, notif_message, notif_appname):
	notification.notify(
	    title='WEBFLINGER!:' + notif_title,
	    message=notif_message,
	    app_name=notif_appname,
	    app_icon='Database/images/system/notif_popup.png' + ('ico' if platform == 'win' else 'png')
	)


########################################
## Colors
########################################
## had to code the json import due to circular import

r = open("Database/config/webflinger_config/config.json", "r")
json_str = (r.read())
data = json.loads(json_str)
key_data = (data["terminal_color"])
r.close()

if key_data == "random":
	colors = ['red','blue','green', 'purple', 'yellow', 'bright_magenta', 'green3', "sky_blue2", "gold3", "orange3"]
	random_color = random.choice(colors)
else:
	random_color = key_data
#print(random_color)

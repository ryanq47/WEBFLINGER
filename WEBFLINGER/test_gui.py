
import main
import bedb
import pyfiglet
import utility
from datetime import datetime

from rich import box
from rich.align import Align
from rich.console import Console, Group
from rich.layout import Layout
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.syntax import Syntax
from rich.table import Table
from rich.text import Text
import os



rand_color = utility.random_color


########################################
## Imports
########################################



def import_refresh():
    f = open("slap_data/slap_tmp/gui_ip_tmp", "r")
    import_refresh.targetIP = f.read()
    f.close()
    
 	## -- loading ports from DB -- ##   
    bedb.loadCOLUMN("slap_db","slap_ip_table", import_refresh.targetIP,'open_ports')
    import_refresh.gui_ports = bedb.loadCOLUMN.key_data
	
	## -- loading services from DB -- ##
    bedb.loadCOLUMN("slap_db","slap_ip_table", import_refresh.targetIP,'services')	
    import_refresh.gui_services = bedb.loadCOLUMN.key_data

	## -- loading scanned range from DB -- ##
    bedb.loadCOLUMN("slap_db","slap_ip_table", import_refresh.targetIP,'scanned_range')	
    import_refresh.range_scan = bedb.loadCOLUMN.key_data


    f = open("slap_data/slap_tmp/ping.tmp", "r")
    import_refresh.ping = f.read()
    f.close()
    ## -- plugin imports -- ##
    f = open("slap_data/slap_tmp/nmap.tmp", "r")
    import_refresh.nmap_scan = f.read()
    f.close()

    bedb.loadCOLUMN("slap_db","slap_ip_table", import_refresh.targetIP, "nmap_scan") #<-- can put any variable here for any plugin
    import_refresh.gui_main = bedb.loadCOLUMN.key_data
    
import_refresh()

## Placeholders/variable retrieval for import_refresh
gui_ports = import_refresh.gui_ports
gui_services = import_refresh.gui_services
targetIP = import_refresh.targetIP
range_scan = import_refresh.range_scan
ping = import_refresh.ping
nmap_scan = import_refresh.nmap_scan
gui_main = import_refresh.gui_main


console = Console()


ascii_banner = pyfiglet.figlet_format(targetIP, font = "standard", width = 1000)
#print(title_color + ascii_banner)
########################################
## Main Layout
########################################
def make_layout() -> Layout:
    """Define the layout."""
    layout = Layout(name="root")

    layout.split(
        Layout(name="header", size=3), ## top blue
        Layout(name="main", ratio=2),
        Layout(name="footer", size=8), ## distance from bottom of term
    )
    layout["main"].split_row(
        Layout(name="side"),
        Layout(name="body", ratio=2, minimum_size=60), # slap! panel
    )
    layout["side"].split(Layout(name="box1"), Layout(name="box2"))
    return layout

## ----------------------------------------
	## Top right panel
## ----------------------------------------
def make_slap_main() -> Panel:
    """Some example content."""
    slap_main = Table.grid(padding=1)
    slap_main.add_column(style=rand_color, justify="left") ## text color
    slap_main.add_column(no_wrap=True)

    import_refresh()

    slap_main.add_row(
        #nmap_scan,
        gui_main,
    )
    
    
    #slap_main.add_row(
    #    "GitHub: [u blue link=https://github.com/ryanq47]https://github.com/ryanq47",
    #)


    #intro_message = Text.from_markup(
    #    """Consider supporting my work via Github Sponsors (ask your company / organization), or buy me a coffee to say thanks. - Will McGugan"""
    #)


    ## Not sure what theese do
    message = Table.grid(padding=1)
    message.add_column()
    message.add_column(no_wrap=True)
    message.add_row(slap_main)

## Panel design/layout
    message_panel = Panel(
        Align.left( ## aligns which side inside panel text is
            Group(slap_main), #, "\n", Align.left(slap_main)),
            vertical="top", ## assigns hieght
        ),
        box=box.ROUNDED,
        padding=(1, 2),
        title="[b red]Full NMAP output",
        border_style=rand_color,
    )
    return message_panel
########################################
## Left panel (box1) Scan
########################################
def make_slap_scan() -> Panel:
    """Some example content."""
    slap_scan = Table.grid(padding=1)
    slap_scan.add_column(style=rand_color, justify="left")
    slap_scan.add_column(no_wrap=True)



    slap_scan.add_row(
        "IP address:",
        range_scan,
        "Open Ports: ",
         gui_ports,
        "Services: ",
         gui_services,
    )
    
    
    #slap_main.add_row(
    #    "GitHub: [u blue link=https://github.com/ryanq47]https://github.com/ryanq47",
    #)


    #intro_message = Text.from_markup(
    #    """Consider supporting my work via Github Sponsors (ask your company / organization), or buy me a coffee to say thanks. - Will McGugan"""
    #)


    ## Not sure what theese do
    message = Table.grid(padding=1)
    message.add_column()
    message.add_column(no_wrap=True)
    message.add_row(slap_scan)

## Panel design/layout
    message_panel = Panel(
        Align.center( ## aligns which side inside panel text is
            Group(slap_scan), #, "\n", Align.left(slap_main)),
            vertical="middle", ## assigns hieght
        ),
        box=box.ROUNDED,
        padding=(1, 2),
        title="[b red]SCAN",
        border_style=rand_color,
    )
    return message_panel
    
########################################
## Bottom Left (IP addr)
########################################
def make_slap_targetIP() -> Panel:
    """Some example content."""
    slap_targetIP = Table.grid(padding=1)
    slap_targetIP.add_column(style=rand_color, justify="left")
    slap_targetIP.add_column(no_wrap=True)



    slap_targetIP.add_row(
        ascii_banner +     "                                                                                                                                                                                                                                                                                                                                                                                                      ",
    ## NOte! this massive empty string^^ is so there is space for the text to be displayted, otherwise it gets cut off
    )
    
    
    #slap_main.add_row(
    #    "GitHub: [u blue link=https://github.com/ryanq47]https://github.com/ryanq47",
    #)


    #intro_message = Text.from_markup(
    #    """Consider supporting my work via Github Sponsors (ask your company / organization), or buy me a coffee to say thanks. - Will McGugan"""
    #)


    ## Not sure what theese do
    message = Table.grid(padding=1)
    message.add_column()
    message.add_column(no_wrap=True)
    message.add_row(slap_targetIP)

## Panel design/layout
    message_panel = Panel(
        Align.center( ## aligns which side inside panel text is
            Group(slap_targetIP), #, "\n", Align.left(slap_main)),
            vertical="top", ## assigns hieght
        ),
        box=box.ROUNDED,
        padding=(-2, -2),
        title="[b red]Target:",
        border_style=rand_color,
    )
    return message_panel
########################################
## middle left (ping)
########################################




def make_slap_ping() -> Panel:
    """Some example content."""
    slap_ping = Table.grid(padding=1)
    slap_ping.add_column(style=rand_color, justify="left")
    slap_ping.add_column(no_wrap=True)



    slap_ping.add_row(
        ping,
    )

    
    #slap_main.add_row(
    #    "GitHub: [u blue link=https://github.com/ryanq47]https://github.com/ryanq47",
    #)


    #intro_message = Text.from_markup(
    #    """Consider supporting my work via Github Sponsors (ask your company / organization), or buy me a coffee to say thanks. - Will McGugan"""
    #)


    ## Not sure what theese do
    message = Table.grid(padding=1)
    message.add_column()
    message.add_column(no_wrap=True)
    message.add_row(slap_ping)

## Panel design/layout
    message_panel = Panel(
        Align.center( ## aligns which side inside panel text is
            Group(slap_ping), #, "\n", Align.left(slap_main)),
            vertical="middle", ## assigns hieght
        ),
        box=box.ROUNDED,
        padding=(1, 2),
        title="[b red]PING test",
        border_style=rand_color,
    )
    return message_panel
## The header
########################################
## Header
########################################
class Header:
    """Display header with clock."""

    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="center", ratio=1)
        grid.add_column(justify="right")
        grid.add_row(
            "[b]" + targetIP + "[/b] Info - press ENTER to exit to SLAP",
            datetime.now().ctime().replace(":", "[blink]:[/]"),
        )
        return Panel(grid, style="white on blue")



########################################
## Jobs (progress bar)
########################################
## Jobs (bottom)

job_progress = Progress(
    "{task.description}",
    SpinnerColumn(),
    BarColumn(),
    TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
)
job_progress.add_task("[green]Bruteforce")
job_progress.add_task("[magenta]Exploit", total=200)
job_progress.add_task("[cyan]DDOS", total=400)

total = sum(task.total for task in job_progress.tasks)
overall_progress = Progress()
overall_task = overall_progress.add_task("All Jobs", total=int(total))

progress_table = Table.grid(expand=True)
progress_table.add_row(
    Panel(
        overall_progress,
        title="Overall Progress",
        border_style="green",
        padding=(2, 2),
    ),
    Panel(job_progress, title="[b]Jobs", border_style="red", padding=(1, 2)),
)



## -- The update for the panels I thinik
########################################
## Layout final
######################################## 

layout = make_layout()
layout["header"].update(Header())
layout["body"].update(make_slap_main())
layout["box2"].update(make_slap_ping())
#layout["box2"].update(Panel(make_syntax(), border_style="green")) -->> may be cool to have this show the raw config file
#layout["box1"].update(Panel(layout.tree, border_style="red"))
layout["box1"].update(make_slap_scan())


layout["footer"].update(make_slap_targetIP())


from rich.live import Live
from time import sleep

#layout

########################################
## this SHOWS the graph until sleep stops
######################################## 



with Live(layout, refresh_per_second=10, screen=True):
    #print('hi')
    #pass
    #print("1")
    #statement = input()
    #if statement == "q":
        #print('hi')
    input("Press enter to continue...")
    #sleep(1000000)






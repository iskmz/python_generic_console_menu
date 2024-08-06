from enum import Enum
import os			# needed for "cls" only
import keyboard		# to be installed by: pip install keyboard
import time			# NOT needed if there's no timer at init
import threading	# NOT needed if there's no timer at init


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# DO NOT CHANGE the following Enum classes, as they define the default values of console colors  - - - - - - - - - - - - - - - - - - - -  #
class FG_COLORS(Enum): # fore-ground colors
	BLACK,RED,GREEN,YELLOW,BLUE,MAGENTA,CYAN,WHITE = 30,31,32,33,34,35,36,37  	# basic colors
	BR_BLACK,BR_RED,BR_GREEN,BR_YELLOW,BR_BLUE,BR_MAGENTA,BR_CYAN,BR_WHITE = 90,91,92,93,94,95,96,97 # BR_: Bright colors
class BG_COLORS(Enum): # back-ground colors 
	BLACK,RED,GREEN,YELLOW,BLUE,MAGENTA,CYAN,WHITE = 40,41,42,43,44,45,46,47  	# basic colors
	BR_BLACK,BR_RED,BR_GREEN,BR_YELLOW,BR_BLUE,BR_MAGENTA,BR_CYAN,BR_WHITE = 100,101,102,103,104,105,106,107 # BR_: Bright colors
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #


# a simple console-menu GENERIC script to run all the code you need without GUI overhead

# it's a SELECT-menu , using up/down keys to navigate and ENTER to select

# once an item is selected , menu disappears (clear-screen) and the script of the function selected runs
	# (could change this behavior , and keep the menu shown in CONSTANTS section)

# no sub-menus are provided , but the same idea could be expanded programmatically to include sub-menus
	# for example: inside the menu-selected-function could run another different copy of this script as a sub-menu

# code below was collected from many different sources on stackoverflow / github and over the web
# tested and works on a windows 10 OS , might not on other systems , or may need some adjustments


# ------------------ Functions to run from MAIN-MENU --------------------------------- #


# each func(): represents a menu item's selection (i.e. the code that runs after selection) 
# it could run more complex sub-functions or external scripts
# add or remove or change names , as needed 


def func1():
	os.system("submenu_1.py")
	
def func2():
	os.system("submenu_2.py")

def func3():	
	os.system("submenu_3.py")

def func4():
	os.system("submenu_4.py")
	
	
# -------------------------- menu ITEMS & mapping to functions ------------------------ #


# should map menu-item names to the EXACT name of the function above , WITHOUT parenthesis -> () !! 

my_menu = {

		"Sub-menu 1":func1,		#0
		"Sub-menu 2":func2,		#1
		"Sub-menu 3":func3,		#2
		"Sub-menu 4":func4		#3
	
	}


# -------------------------- CONSTANTS to define menu properties ----------------------- #

CONSOLE_TITLE = "MAIN_MENU"	# a text to define console window's title

DEFAULT_SELECTION = 2 	# an integer between 0  to  len(my_menu)-1  # defines default item to be selected (i.e. highlighted) automatically at init
						# corresponds to the numbers beside the my_menu dictionary defined above !  # 0,1,2,3 .. etc 

TIMER = False 			# True/False: whether or not a timed msg shows under the menu at init. regarding DEFAULT_SELECTION: which runs automatically after time given ends
TIME_SEC = 11 			# works only if TIMER=True # time of msg for DEFAULT_SELECTION , defined in SECONDS , that when run-out DEFAULT_SELECTION is chosen automatically


INCLUDE_QUIT = True 	# True/False, to add a "quit" item at the bottom of the menu, or not to add one
QUIT_TXT = "Exit!"		# works only if INCLUDE_QUIT=True # the text shown of the QUIT menu item !

SELECTION_FG_COLOR = FG_COLORS.BLACK	# defines foreground color of item currently selected (highlighted) , check color palette defined at top of code
SELECTION_BG_COLOR = BG_COLORS.BR_CYAN	# defines background color of item currently selected (highlighted) , check color palette defined at top of code

KEEP_MENU = False # True/False , if True: then after selection of any item and item-code runs to its end, then menu keeps working (& shown at top) to select any item again!

WIDTH_FACTOR = 32  	# an integer between 0 and half (or better: less than half) of console width (in characters-count) 
					# depends on menu-item's longest text  # better to adjust slightly and check appearance !

NO_BORDERS = False 			# True/False , if True: no borders for the menu, only a list of items and selection-highlight
DOUBLE_BORDERS = False		# True/False , only works if NO_BORDERS=False # if true then borders are double-lined and Not the default solid-single borders (if False)
ROUND_CORNERS = True		# True/False , only works if NO_BORDERS=False AND DOUBLE_BORDERS=False 
							# if true then corners of menu are rounded , otherwise they are 'pointy' (90 degrees angle)
COMPACT_ITEMS_LIST = True 	# True/False , if True: items list is compact, no spaces between items , suitable for menus with many items!

LEFT_TABS = 1	# how many TABS the menu is spaced from the left side of the console window
TOP_LINES = 2	# how many lines the menu is spaced from the top of the console window


# -------------------------- generic-menu code  --------------------------------------- #


# NO need to change all of the code below

# it defines and runs the menu as described by the above parameters (constants,items,functions...)



menu = list(my_menu.keys())
menu_selection = list(my_menu.values()) # function names, mapped to menu-items above 
if INCLUDE_QUIT:
	menu.append(QUIT_TXT)
	menu_selection.append(exit)

max_menu_item_len = max([len(item) for item in menu])


if (DEFAULT_SELECTION<0 or DEFAULT_SELECTION>=len(menu)): # a check ... just in case ! 
	DEFAULT_SELECTION=0
selected = DEFAULT_SELECTION

space_factor = WIDTH_FACTOR

if not NO_BORDERS:
	HBB = "\u2550" if DOUBLE_BORDERS else "\u2500"	# HBB: Horizontal Border Block  #  "\u2500": solid ,  "\u2550": double
	VBB = "\u2551" if DOUBLE_BORDERS else "\u2502" 	# VBB: Vertical Border Block  	#  "\u2502": solid ,  "\u2551": double
	if ROUND_CORNERS and not DOUBLE_BORDERS:
		TLC,TRC,BLC,BRC = "\u256d","\u256e","\u2570","\u256f"  # TLC: Top Left Corner , TRC: Top Right , BLC: Bottom Left , BRC: Bottom Right
	elif DOUBLE_BORDERS: # (double + pointy) corners
		TLC,TRC,BLC,BRC = "\u2554","\u2557","\u255a","\u255d"
	else: # (single + pointy) corners 
		TLC,TRC,BLC,BRC = "\u250c","\u2510","\u2514","\u2518"
	# define top,bottom,left,right borders from the building-blocks defined above
	top_b = TLC+HBB*(max_menu_item_len+space_factor*2)+TRC
	left_b = "\t"*LEFT_TABS + VBB
	right_b = VBB
	bottom_b = BLC+HBB*(max_menu_item_len+space_factor*2)+BRC
else:
	left_b = "\t"*LEFT_TABS
	right_b = ""

space_item = " "*max_menu_item_len
select_sp_left = "\x1b["+str(SELECTION_FG_COLOR.value)+";"+str(SELECTION_BG_COLOR.value)+"m" + " "*space_factor
select_sp_right = " "*space_factor+"\x1b[0m"  	# 0: resets all colors , after selection line ends
unselect_sp = " "*space_factor

def show_menu():
	global selected
	os.system("cls")
	print("\n"*TOP_LINES,end="")
	if not NO_BORDERS:
		print("\t"*LEFT_TABS + top_b)
	for i in range(len(menu)):
		x_space = max_menu_item_len-len(menu[i])
		left_sp , right_sp = " "*(x_space//2) , " "*(x_space-x_space//2)
		menu_item = left_sp+menu[i]+right_sp
		left = select_sp_left if selected == i else unselect_sp
		right = select_sp_right if selected == i else unselect_sp
		if not COMPACT_ITEMS_LIST:
			print("{3}{0}{2}{1}{4}".format(left,right,space_item,left_b,right_b))
		print("{3}{0}{2}{1}{4}".format(left,right,menu_item,left_b,right_b))
		if not COMPACT_ITEMS_LIST:
			print("{3}{0}{2}{1}{4}".format(left,right,space_item,left_b,right_b))
	if not NO_BORDERS:
		print("\t"*LEFT_TABS + bottom_b)
	print(" * select an item using up/down/enter keys")


def up():
	global selected
	if selected==0:
		selected=len(menu)-1
	else:
		selected -= 1
	show_menu()

def down():
	global selected
	if selected==len(menu)-1:
		selected=0
	else:
		selected += 1
	show_menu()

def goto_selection():
	if not KEEP_MENU:
		os.system("cls")	
	menu_selection[selected]()
	if not KEEP_MENU:
		exit()

def menu_loop():
	while True:
		x = keyboard.read_event(suppress=True)
		if x.event_type == "up":
			continue
		else:
			if x.name=='up':
				up()
			elif x.name=='down':
				down()
			elif x.name=='enter':
				goto_selection()
			else:
				show_menu()


keypress = False
done_counting = False
waiting_time = TIME_SEC # seconds
def show_auto_msg():
	global keypress
	global done_counting
	counter = waiting_time
	while counter>0 and not keypress:
		print(" * or wait ",counter," seconds for "+menu[DEFAULT_SELECTION]+" to run ...  ")
		time.sleep(1)
		counter -= 1
		print ("\x1b[A\x1b[A")	# an ANSI Escape Sequence to move-cursor up a line and re-write the counter_seconds line 
		# for further details: https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797  
	if not keypress:
		done_counting = True
		goto_selection()

def stop_auto_msg():
	global keypress
	global done_counting
	while True and not done_counting:
		if keyboard.is_pressed('up') or keyboard.is_pressed('down') or keyboard.is_pressed('enter'):
			keypress=True
			break
	if not done_counting:
		menu_loop()

def main_menu():
	os.system("title "+CONSOLE_TITLE)
	show_menu()
	if TIMER:
		t1 = threading.Thread(target=show_auto_msg)
		t2 = threading.Thread(target=stop_auto_msg)
		t1.start()
		t2.start()
	else:
		menu_loop()


# ------------------------ MAIN ------------------------------------------ #

main_menu()

# ------------------------------------------------------------------------ #
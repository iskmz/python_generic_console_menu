from enum import Enum
import os
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
# a customizable menu, with options to change colors, borders, msgs ... etc ... 

# once an item is selected , menu disappears (clear-screen) and the script of the function selected runs
	# > could change this behavior , and keep the menu shown in CONSTANTS section <

# no sub-menus are provided , but the same idea could be expanded programmatically to include sub-menus
	# for example: inside the menu-selected-function could run another different copy of this script as a sub-menu  (check "sub_menu_example" folder)

# code below was collected in part from many different sources on stackoverflow / github and over the web
# tested and works on a windows 10 OS , might not on other systems , or may need some adjustments


# ------------------ Functions to run from MAIN-MENU --------------------------------- #


# each func(): represents a menu item's selection (i.e. the code that runs after selection) 
# it could run more complex sub-functions or external scripts
# add or remove or change names , as needed 


def func1():
	print("function 1")
	
def func2():
	print("function 2")

def func3():	
	print("function 3")

def func4():
	print("function 4")
	
	
	
# -------------------------- menu ITEMS & mapping to functions ------------------------ #


# should map menu-item names to the EXACT name of the function above , WITHOUT parenthesis -> () !! 

my_menu = {

		"Function 1":func1,			#0
		"F2":func2,					#1
		"Fun3 (Default)":func3,		#2
		"f4":func4					#3
	
	}


# -------------------------- CONSTANTS to define menu properties ----------------------- # --------  (27) in TOTAL , as of 2024-08-07 , 16:44 local time ------ #

# 1 
# a text to define console window's title
CONSOLE_TITLE = "MAIN_MENU"
# 2 
# an integer between 0  to  len(my_menu)-1  # defines default item to be selected (i.e. highlighted) automatically at init
# corresponds to the numbers beside the my_menu dictionary defined above !  # 0,1,2,3 .. etc 
DEFAULT_SELECTION = 0 	
# 3
# True/False: whether or not a timer-msg shows under the menu at init. regarding DEFAULT_SELECTION: which runs automatically after time given ends
TIMER = True
# 4
# works only if TIMER=True # time of msg for DEFAULT_SELECTION , defined in SECONDS , that when run-out DEFAULT_SELECTION is chosen automatically
TIME_SEC = 33
# 5
# True/False: whether or not a msg prompt for up/down/enter keys is shown under the menu or not 
SELECTION_MSG = True
# 6
# True/False, to add a "quit" item at the bottom of the menu, or not to add one
INCLUDE_QUIT = True
# 7
# works only if INCLUDE_QUIT=True # the text shown of the QUIT menu item !
QUIT_TXT = "Quit"
# 8
# defines foreground color of item currently selected (highlighted) , check color palette defined at top of code
SELECTION_FG_COLOR = FG_COLORS.BLACK
# 9
# defines background color of item currently selected (highlighted) , check color palette defined at top of code
SELECTION_BG_COLOR = BG_COLORS.BR_GREEN
# 10
# True/False , if True: then after selection of any item and item-code runs to its end, then menu keeps working (& shown at top) to select any item again!
KEEP_MENU = False
# 11
# an integer between 0 and half (or better: less than half) of console width (in characters-count) 
# defines menu-box width  , which also depends on menu-item's longest text (and also on LEFT/RIGHT WHITESPACES defined below)
# better to adjust slightly and check appearance !
WIDTH_FACTOR = 16
# 12
# True/False , if True: no borders for the menu, only a list of items and selection-highlight
NO_BORDERS = False
# 13
# True/False , NO_BORDERS=True overrides this one, but if NO_BORDERS=False AND NO_TOP_BORDER=True, then only top border is removed
NO_TOP_BORDER = False
# 14
# True/False , NO_BORDERS=True overrides this one, but if NO_BORDERS=False AND NO_BOTTOM_BORDER=True, then only bottom border is removed
NO_BOTTOM_BORDER = False
# 15
# True/False , NO_BORDERS=True overrides this one, but if NO_BORDERS=False AND NO_LEFT_BORDER=True, then only left border is removed
NO_LEFT_BORDER = False	
# 16
# True/False , NO_BORDERS=True overrides this one, but if NO_BORDERS=False AND NO_RIGHT_BORDER=True, then only right border is removed
NO_RIGHT_BORDER = False
# 17
# True/False , only works if NO_BORDERS=False # if true then borders are double-lined and Not the default solid-single borders (if False)
DOUBLE_BORDERS = False
# 18
# True/False , removes corners if True , suitable when left+right borders are removed , so that no corners are shown
NO_CORNERS = False
# 19
# True/False , only works if (NO_BORDERS=False AND DOUBLE_BORDERS=False AND NO_CORNERS=False)
# if true then corners of menu are rounded , otherwise they are 'pointy' (90 degrees angle)
ROUND_CORNERS = True	
# 20
# True/False , if True: items list is compact, no spaces between items (i.e. NO top/bottom spaces) ... suitable for menus with many items!
COMPACT_ITEMS_LIST = False
# 21
# how many TABS the menu is spaced from the left side of the console window
LEFT_TABS = 3
# 22
# how many lines the menu is spaced from the top of the console window
TOP_LINES =	2
# 23
# True/False , defines items alignment , takes precedence (if True) over ALIGN_RIGHT !
ALIGN_LEFT = False
# 24
# True/False,  defines items alignment , works only if ALIGN_LEFT=False , i.e. LEFT takes precedence !
# if both LEFT/RIGHT are false then items are CENTERED by default !
ALIGN_RIGHT = False
# 25
# True by default: menu items are CENTERED in the menu , regardless of their alignment relative to each other (LEFT/RIGHT/CENTER)
# if FALSE: then position of menu items depends on their alignment constants above (LEFT , RIGHT or CENTER: if both False)
# could use the false option to align items to the EXTREME left or EXTREME right of the menu box ! 						
CENTER_IN_MENU = True
# 26
# adds as much whitespace:" " , as the value in the constant to the left of each menu-item's name defined in the previous section (my_menu dictionary)
WHITESPACE_LEFT_ITEM = 0
# 27
# adds as much whitespace:" " , as the value in the constant to the right of each menu-item's name defined in the previous section (my_menu dictionary)		
WHITESPACE_RIGHT_ITEM = 0	
					# both items above (26+27) are suitable when items are aligned to extreme left or right, to move a bit away from menu-box
					# also items could stay centered relative to each other and moved to the LEFT or RIGHT of the menu-box by changing left/right spaces proportions


# ----------------------------------------------------------------------------------------------------------------------------------------- #
# -------------------------- generic-menu code  --------------------------------------- # ---------- NO CHANGES BELOW THIS LINE ----------- #
# ----------------------------------------------------------------------------------------------------------------------------------------- #

# NO need to change any of the code below , but feel free to do so , at your own risk  :D

# code below defines and runs the menu as described by the above parameters (constants,items,functions...)


menu = list(my_menu.keys())
menu_selection = list(my_menu.values()) # function names, mapped to menu-items above 
if INCLUDE_QUIT:
	menu.append(QUIT_TXT)
	menu_selection.append(exit)

for i in range(len(menu)):
	menu[i] = " "*WHITESPACE_LEFT_ITEM + menu[i] + " "*WHITESPACE_RIGHT_ITEM

max_menu_item_len = max([len(item) for item in menu])

if (DEFAULT_SELECTION<0 or DEFAULT_SELECTION>=len(menu)): # a check ... just in case ! 
	DEFAULT_SELECTION=0
selected = DEFAULT_SELECTION

space_factor = WIDTH_FACTOR

if not NO_BORDERS:
	HBB = "\u2550" if DOUBLE_BORDERS else "\u2500"	# HBB: Horizontal Border Block  #  "\u2500": solid ,  "\u2550": double
	VBB = "\u2551" if DOUBLE_BORDERS else "\u2502" 	# VBB: Vertical Border Block  	#  "\u2502": solid ,  "\u2551": double
	if NO_CORNERS:
		TLC,TRC,BLC,BRC = " " , " ", " ", " " 	# TLC: Top Left Corner , TRC: Top Right , BLC: Bottom Left , BRC: Bottom Right
	elif ROUND_CORNERS and not DOUBLE_BORDERS:
		TLC,TRC,BLC,BRC = "\u256d","\u256e","\u2570","\u256f"  
	elif DOUBLE_BORDERS: # (double + pointy) corners
		TLC,TRC,BLC,BRC = "\u2554","\u2557","\u255a","\u255d"
	else: # (single + pointy) corners 
		TLC,TRC,BLC,BRC = "\u250c","\u2510","\u2514","\u2518"
	# define top,bottom,left,right borders from the building-blocks defined above  
	# for further details: https://en.wikipedia.org/wiki/Box-drawing_characters#Unicode
	top_b = TLC+HBB*(max_menu_item_len+space_factor*2)+TRC
	left_b = "\t"*LEFT_TABS
	left_b += VBB if not NO_LEFT_BORDER else " "
	right_b = VBB if not NO_RIGHT_BORDER else " "
	bottom_b = BLC+HBB*(max_menu_item_len+space_factor*2)+BRC
else:
	left_b = "\t"*LEFT_TABS
	right_b = ""

space_item = " "*max_menu_item_len
select_sp_left = "\x1b["+str(SELECTION_FG_COLOR.value)+";"+str(SELECTION_BG_COLOR.value)+"m"
select_sp_left += " "*space_factor if CENTER_IN_MENU else ""
select_sp_right = " "*space_factor if CENTER_IN_MENU else ""
select_sp_right += "\x1b[0m"  	# 0: resets all colors , after selection line ends
unselect_sp_left = " "*space_factor if CENTER_IN_MENU else ""
unselect_sp_right = " "*space_factor if CENTER_IN_MENU else ""

if not CENTER_IN_MENU:
	if not ALIGN_LEFT and not ALIGN_RIGHT:  # items are centered AGAIN (despite not being CENTER_IN_MENU , alignment is CENTER
		select_sp_left , select_sp_right  = select_sp_left + " "*space_factor , " "*space_factor + select_sp_right
		unselect_sp_left , unselect_sp_right = " "*space_factor , " "*space_factor
	elif ALIGN_LEFT:
		select_sp_right  =  " "*(space_factor*2) + select_sp_right
		unselect_sp_right = " "*(space_factor*2)
	elif ALIGN_RIGHT:
		select_sp_left += " "*(space_factor*2)
		unselect_sp_left = " "*(space_factor*2)

def show_menu():
	global selected
	os.system("cls")
	print("\n"*TOP_LINES,end="")
	if not NO_BORDERS and not NO_TOP_BORDER:
		print("\t"*LEFT_TABS + top_b)
	for i in range(len(menu)):
		x_space = max_menu_item_len-len(menu[i])
		left_sp , right_sp = " "*(x_space//2) , " "*(x_space-x_space//2)
		if not ALIGN_LEFT and not ALIGN_RIGHT:  # items are centered 
			menu_item = left_sp+menu[i]+right_sp
		elif ALIGN_LEFT: # works even if ALIGN_RIGHT is also TRUE , i.e. LEFT takes precedence ! 
			menu_item = menu[i] + left_sp + right_sp
		elif ALIGN_RIGHT:
			menu_item = left_sp + right_sp + menu[i]				
		left = select_sp_left if selected == i else unselect_sp_left
		right = select_sp_right if selected == i else unselect_sp_right
		if not COMPACT_ITEMS_LIST:
			print("{3}{0}{2}{1}{4}".format(left,right,space_item,left_b,right_b))
		print("{3}{0}{2}{1}{4}".format(left,right,menu_item,left_b,right_b))
		if not COMPACT_ITEMS_LIST:
			print("{3}{0}{2}{1}{4}".format(left,right,space_item,left_b,right_b))
	if not NO_BORDERS and not NO_BOTTOM_BORDER:
		print("\t"*LEFT_TABS + bottom_b)
	if SELECTION_MSG:
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
		print(" * after ",counter," seconds , "+menu[DEFAULT_SELECTION].strip()+" will run ...  ")
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

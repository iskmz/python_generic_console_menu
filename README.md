# python generic console menu


<i> last update: 2024-08-07 , 20:09 local time</i>


+ a simple GENERIC menu for console (commandline) users
+ consists of a SINGLE python script file:  [python_generic_console_menu.py](python_generic_console_menu.py)
+ command-line based , using ANSI Escape Sequences for coloring and drawing boxes/borders without GUI overhead
  - check [HERE](https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797  ) for further details about ANSI ESCAPE SEQUENCES
  - check [HERE](https://en.wikipedia.org/wiki/Box-drawing_characters) for further details about box-drawing characters used
+ an item pick selection menu , or a list to select from ,  using up/down keys to navigate and ENTER to select
+ a customizable menu, with options to change colors, borders, msgs
  - check CONSTANTS section to modify how the menu looks and behaves <b>(lines 70-163)</b>
+ could add as much menu items as needed and map them to the functions required which could run anything from python scripts to external code
  - check items/functions sections to define menu items and map them to the needed functions to run <b>(lines 33-69)</b>
+ once an item is selected , menu disappears (clear-screen) and the script of the function selected runs
  - could change this behavior , and keep the menu shown (in CONSTANTS section)
+ NO sub-menus are provided inherently , but the same idea could be expanded programmatically to include sub-menus
  - for example: inside the menu-selected-function , you could run another different copy of this script as a sub-menu
  - for further details check "[sub_menu_example](./sub_menu_example)" folder provided
+ code used for this script was collected , in part, from many different sources on stackoverflow / github and over the web
+ tested and works on a windows 10 OS , might not on other systems , or may need some adjustments
+ check comments inside the script for further details on how to use/modify it for your purposes
+ a usage example could be found in the repo [beeps_and_drawings](https://github.com/iskmz/beeps_and_drawings/) :-
  - [beepnotes2__menu.py](https://github.com/iskmz/beeps_and_drawings/blob/main/beepnotes2__menu.py)
  - [draw__menu.py](https://github.com/iskmz/beeps_and_drawings/blob/main/draw__menu.py)

----------------------

<img src="https://github.com/user-attachments/assets/6cd426e6-8746-4d87-92b7-93ea270ff1e9" /><br/><br/>
<img src="https://github.com/user-attachments/assets/151dbb72-32e0-412d-996f-52d4dc73a4f1" /><br/><br/>
<img src="https://github.com/user-attachments/assets/4c8eceb3-dd35-48c3-bc84-951da53a8e8d" /><br/><br/>
<img src="https://github.com/user-attachments/assets/154e209c-839f-409a-8d80-4d8c9926c515" /><br/><br/>
<img src="https://github.com/user-attachments/assets/760e463b-706f-49e7-ab0a-3d109dd5f083" /><br/><br/>

----------------------

#!python3

""" 
pyautogui:
PyAutoGUI lets your Python scripts control the mouse and 
keyboard to automate interactions with other applications. 
The API is designed to be as simple. 
PyAutoGUI works on Windows, macOS, and Linux, and runs on Python 2 and 3.
https://pyautogui.readthedocs.io/en/latest/index.html

Once we install it, we can explore some of the functionality available
in the pyautogui methods.  The documentation shows good information on 
a lot of the commands, but some of the methods that will be most useful
to us:

moveTo(x,y)
click()
click(x,y,clicks,interval,button) optional arguments can be included!
alert()
confirm()
prompt()
locateOnScreen() looks for an image on screen and returns the first instance (left, top, width, height)
locateAllOnScreen() looks for an image on screen and returns a tuple of instances
locateCenterOnScreen() looks for an image and returns the (x,y) of the first instance
    - check out the documentation for more information on the screen image locate methods
getpixel(x,y) returns the color of the pixel at a particular location

note: I find typing in "pyautogui" a lot to be quite time consuming, so will
usually assign a shorter name to the module.

A useful function is the "info" method to help gather information about
your screen

"""
#p.mouseInfo()
import pyautogui as p 
import time 


#locations of upgrades
burrow=(1320,495)
hoard=(1320,555)
dam=(1320,615)
pen=(1600,495)
farm=(1600,555)
puddles=(1600,615) 
upgrade_list=[burrow,hoard,dam,pen,farm,puddles]
index=0

#function that cycles through the upgrades
def click():
    global index
    p.click(upgrade_list[index])
    index = index + 1
    
    if index>5:
        index=0 

#locations f resources/resouce gathering buttons 
shrimp=(1300,330)
twigs=(1500,320)
pebbles=(1300,380)
resource_button=[shrimp,twigs,pebbles]
resource_list=[(1000,330),(1000,360),(1000,390)]
index1=0

#block cycles through the resources until all bars are full
#full resource bar=(0,125,0)
def resources():
    global index1
    x,y = resource_list[index1]
    p.click(resource_button[index1])
    if p.pixelMatchesColor(x,y,(0,125,0)):
        index1= index1 + 1
        
        if index1>2:
            index1=0
            print("Pausing for 3 seconds...",end="")
            print("Checking for updates")
            time.sleep(3)
            click()
while True:
    resources()

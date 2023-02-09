 # -*- coding: utf-8 -*-

# This is a script that changes the image on the desktop.
# Also responsible for minimizing to tray.

import os
import sys
import time
import ctypes
import pystray
import logging
import threading
import traceback
import configparser
from PIL import Image


logging.basicConfig(
	level=logging.INFO,
	format='[%(asctime)s] [%(levelname)s] | %(message)s',
	datefmt='%Y-%m-%d %H:%M:%S')

logging.basicConfig(
	level=logging.WARNING,
	format='[%(asctime)s] [%(levelname)s] | %(message)s',
	datefmt='%Y-%m-%d %H:%M:%S')

logging.basicConfig(
	level=logging.ERROR,
	format='[%(asctime)s] [%(levelname)s] | %(message)s',
	datefmt='%Y-%m-%d %H:%M:%S')


# show console (really?)
def show_console():
	ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 1)

# hide console (really?)
def hide_console():
	ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def cls():
	os.system("cls")

# open config file
def openConfig():
	config = configparser.ConfigParser() # init
	config.read("config.ini") # read the config file
	return config # return config object

# if something went wrong
def exceptionExit(exception):
	sys.stdout.write(exception) # print exception in console
	input("Press something to continue...")
	cls()

# get all wallpapers
def get_names():
	config = openConfig()
	img_names = config["DEFAULT"]["images"].split(", ")
	if len(img_names) < 3:
		exceptionExit("Add at least 3 images then restart me.")
		return sys.exit(0)
	return img_names # returns list of wallpaper names

# get timeout from config
def get_timeout():
	config = openConfig()
	return int(config["DEFAULT"]["timeout"])

# change desktop image
def change_wallpaper():
	logging.info("Ready! Now the wallpaper will change every 3 seconds!")
	wallpaper_names = get_names() # get all wallpapers
	timeout = get_timeout() # get timeout
	while True: # INFINITE LOOP, WOW!
		for name in wallpaper_names: # for wp in all wallpapers
			path = os.getcwd()+'\\images\\{}'.format(name) # path to wallpaper
			ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0) # change image (wiiiiindows)
			logging.info(f"WP changed on {name}")
			time.sleep(timeout) # sleeeeeeeeeep

# minimize to tray func
def create_tray_icon():
	logging.info("Minimizing to tray...")
	image = Image.open("wp.ico") # open icon with pillow
	menu_item1 = pystray.MenuItem('Показать консоль', show_console) # new button for tray icon (if you click RMB you'll see it)
	menu_item2 = pystray.MenuItem('Спрятать консоль', hide_console) # another new button
	menu_items = (menu_item1, menu_item2,) # all buttons
	icon = pystray.Icon("WP Changer", image, "WP Changer", menu_items) # setup Icon object
	logging.info("Minimized!")
	icon.run() # MINIMINIMIZE

def starter():
	logging.info("Launching wp changer\n\n")
	hide_console() # hiiiide ugly command prompt
	change_wallpaper() # start changing wallpapers!


try:
	threading.Thread(target=starter).start() # threading because pystray is idiot and i have infinite loop :p
	threading.Thread(target=create_tray_icon).start()
except Exception as e:
	sys.stdout.write(traceback.format_exc())
	sys.stdout.write("Error: " + e)

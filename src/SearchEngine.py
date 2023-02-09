 # -*- coding: utf-8 -*-

# This file is designed to search for images for a given query on the Internet.
# it's not a python plugin, it's a complete image search script!

import os
import sys
import logging
import requests
import traceback
import configparser
from PIL import Image
from google_images_search import GoogleImagesSearch


logging.basicConfig(
	level=logging.INFO,
	format='[%(asctime)s] [%(levelname)s] | %(message)s',
	datefmt='%Y-%m-%d %H:%M:%S')

logging.basicConfig(
	level=logging.WARNING,
	format='[%(asctime)s] [%(levelname)s] | %(message)s',
	datefmt='%Y-%m-%d %H:%M:%S')

# clear console
def cls():
	os.system("cls")

# open config.ini file
def openConfig():
	config = configparser.ConfigParser()
	config.read("config.ini")
	return config

# get api keys for google search
def getKeys(config):
	return config["KEYS"]["api_key"], config["KEYS"]["cx"]

# set search parameters
def search_params(query, req_count):
	_search_params = {
		'q': query,  # query
		'num': req_count, # requests count
		'fileType': 'jpg|png', # image type for wp
		'imgSize': 'huge' # huge size for high image resolution
	}
	return _search_params

# if something went wrong
def exceptionExit(exception):
	sys.stdout.write(exception) # print exception in console
	input("Press something to continue...")
	cls() # clear console

# check if value's type is integer
def checkInt(value, exception):
	try:
		value = int(value)
		return value
	except ValueError:
		return exceptionExit(exception)

# Ask you about search params
def askParams():
	cls()
	sys.stdout.write("Input search query that must contain more than 10 symbols (something like 'Sea wallpapers 1920x1080'):")
	query = input("> ")
	sys.stdout.write("Input images count which you want to get as a result (must be equal 3 or greater):")
	img_count = input("> ")
	img_count = checkInt(img_count, "Images count must be integer.") # i need to return exception if it fails and i didnt use isdigit() method.
	if len(query) <= 10: # if query has not enough symbols restart func
		exceptionExit("Query length must be greater than 10")
		return askParams()
	if img_count < 3: # if image count is less than 3 restart func
		exceptionExit("Image count must be equal 3 or greater")
		return askParams()
	return query, img_count # str and int

# Google search
def googleSearch():
	api_key, cx = getKeys(openConfig()) # getting api_key and cx key
	if len(api_key) == 0 or len(cx) == 0: # check if api keys are not provided
		exceptionExit("Provide an api key and cx key in config.ini. Then restart.")
		return sys.exit(0) # exit if no
	query, req_count = askParams() # ask user
	logging.info(f"Looking for {query} images")
	gis = GoogleImagesSearch(api_key, cx) # init
	gis.search(search_params=search_params(query, req_count)) # let's go!
	results = gis.results()[:req_count] # first {req_count} results (req count is from askParams())
	return results # returns list

# create 'images' directory
def createDir(name):
	if not os.path.exists(name):
		os.makedirs(name)

# download all images that you have found
def dlResults(results):
	logging.info("Preparing to download results... ")
	createDir("images")
	img_names = [] # list of wp names for write to config
	for i, image in enumerate(results):
		image_url = image.url
		response = requests.get(image_url) # request image source
		if response.status_code == 200: # if successfully
			with open(f"images/image_{i}.jpg", "wb") as f:
				f.write(response.content) # add an image to directory
			img = Image.open(f'images/image_{i}.jpg') # open image in pillow for analyzing
			width, height = img.size # get the width and height of image
			if width < 1920 or height < 1080: # check if resolution is greater or equal 1920x1080
				img.close() # close opened image
				os.remove(f'images/image_{i}.jpg') # remove image if bad resolution
				logging.info(f"Image {i} has a bad resolution. Successfully Removed.")
			else:
				img_names.append(f"image_{i}.jpg") # add to list of wp names this file (for write to config)
				logging.info(f"Downloaded: {i}/{len(results)}")
		else:
			logging.warning(f"Failed to download image {i}: {image_url}")
	logging.info("Finished downloading!")
	return img_names # returns list

# adding results to config
def writeResults(img_names):
	logging.info("Preparing to write results")
	config = openConfig() # open config file
	old_images = config["DEFAULT"]["images"].split(", ") # getting a list of old wallpapers from config
	old_images_count = len(old_images)
	if old_images_count > 2:
		logging.info(f"{old_images_count} images was found in config file.")
		for old_image in old_images:
			img_names.append(old_image) # add old wallpapers to new
			logging.info(f"{old_image} added to image names list")
	config['DEFAULT'] = {"images": ", ".join(img_names)[:-1]} # write new wallpapers with old
	logging.info("Finishing adding results to config...")
	with open('config.ini', 'w') as configfile:
		config.write(configfile) # finally add!
	logging.info("Success!")


def launchSearchEngine():
	try:
		images = googleSearch() # seaaaarch
	except Exception as e:
		sys.stdout.write(traceback.format_exc())
		sys.stdout.write(f"Error: " + e)
	try:
		downloaded_images = dlResults(images) # doooownlooooad
	except Exception as e:
		sys.stdout.write(traceback.format_exc())
		sys.stdout.write(f"Error: " + e)
	try:
		writeResults(downloaded_images) # wriiiite results to confiiig
	except Exception as e:
		sys.stdout.write(traceback.format_exc())
		sys.stdout.write(f"Error: " + e)
	finally:
		logging.info("Finished work.")
		input("Press any button to exit")


try:
	launchSearchEngine() # maaain func
except KeyboardInterrupt:
	sys.exit(0)
except Exception as e:
	sys.stdout.write(traceback.format_exc())
	sys.stdout.write(f"Error: " + e)

"""
RUN ME FIRST

@author: lightningb4
@date: 31/12/2019

"""
import tools.prefix as pfx
from termcolor import colored
import json
import os
import time
from random import choice

class Base:

	def __init__(self):
		self.config_data = self.load_data()
		print(self.config_data)

	def load_data(self):
		try:
			cwd = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")
			with open(cwd) as json_file:
				data = json.load(json_file)
				return data
		except FileNotFoundError:
			print("Oops. Looks like the config file doesn't exist. Has it been renamed? Moved?")
			return False

	def load_screen_details(self):
		print(f"SETUP: {self.config_data}")
		allow_config = True if self.config_data is not False else False
		if allow_config:
			if self.config_data['settings']['clear-on-start']:
				os.system("clear")

		# Print that beautiful cliche ascii art
		art = "\n██████╗ ██╗    ██╗██████╗     ███╗   ███╗ █████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗██████╗\n██╔══██╗██║    ██║██╔══██╗    ████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝██╔══██╗\n██████╔╝██║ █╗ ██║██║  ██║    ██╔████╔██║███████║██╔██╗ ██║███████║██║  ███╗█████╗  ██████╔╝\n██╔═══╝ ██║███╗██║██║  ██║    ██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██╔══╝  ██╔══██╗\n██║     ╚███╔███╔╝██████╔╝    ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗██║  ██║\n╚═╝      ╚══╝╚══╝ ╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝"
		print(art)
		if self.config_data is not False:
			try:
				COLOUR = choice(["red", "green", "blue", "yellow", "magenta", "cyan"])
				attr = ['bold', 'blink']
				# Make all the pretty colours :)
				version = colored(f"{self.config_data['version']}", COLOUR, attrs=attr)
				author = colored(f"{self.config_data['author']}", COLOUR, attrs=attr)
				created = colored(f"{self.config_data['date-created']}", COLOUR, attrs=attr)
				updated = colored(f"{self.config_data['last-update']}", COLOUR, attrs=attr)

				print(f"[Version: {version}]\t[Author: {author}]\t[Created: {created}]\t[Updated: {updated}]")

			except KeyError:
				print("Oops. Looks like a key has been mistyped or doesn't exist :/")
		else:
			message = colored("[ERR]", "red") + " The data file has not been read correctly. Enable logs to fix issue!"
			print(message)
			exit(0)

class Setup(Base):

	def __init__(self):
		super().__init__()
		#Create the configuration data:
		self.create_config()
		# Startup screen stuff
		self.load_screen_details()
		# Check if first time setup
		if self.config_data['account']['first-time']:
			print(pfx.NOTE + "Running first time setup. This will erase pwdManager database data if one exists.")
			exit_loop = False

			while not exit_loop:
				start_setup = input(pfx.WARNING + "Are you sure you wish to begin setup [y/n]? ").lower()
				if start_setup not in ['y', 'n']:
					print("Please only enter 'y' or 'n'...")
					continue
				exit_loop = True
				if start_setup == "y":
					print(pfx.NOTE + "Running Setup...")


				else:
					print(pfx.SUCCESS +"Setup aborted!")

	""" 
	TODO: MAKE THIS GENERATE ALL NEEDED CONFIG 
	"""
	def create_config(self):
		pass


class Run(Base):

	def _init__(self):
		self.load_screen_details()

"""
@author: lightningb4
@date: 31/12/2019

"""
import tools.prefix as pfx
from termcolor import colored
import json
import os
import time
from random import choice
from tools import configuration
from tools import action
from storage import sqlalchemy_delcare as sql_dec

class Base:

	def __init__(self):
		failed_message = "Oops. Looks like the config file doesn't exist. Has it been renamed? Moved?"
		self.config_data = configuration.load_data(failed_message)
		print(self.config_data)

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
		# Startup screen stuff
		self.load_screen_details()
		# Check if first time setup
		if self.config_data['account']['reset']:
			msgs = []

			if not configuration.database_exists():
				msgs = ["Running first time setup.", "Database will be created as one has not been detected."]
			else:
				msgs = ["Running RESET (Create New) Mode. This will erase pwdManager database data if one exists.",
			 "If this is first time setup, ignore warning and continue"]

			for msg in msgs:
				print(pfx.NOTE + msg)
			exit_loop = False

			## Infinite loop of asking whether or not to run setup
			while not exit_loop:
				start_setup = input(pfx.WARNING + "Are you sure you wish to begin setup [y/n]? ").lower()
				if start_setup not in ['y', 'n']:
					print("Please only enter 'y' or 'n'...")
					continue
				exit_loop = True
				if start_setup == "y":
					self.all_setup_actions()
					print(pfx.SUCCESS + "Setup finished! Running main body.")
					Run()
				else:
					print(pfx.SUCCESS +"Setup aborted!")

	## Here is where all of the setup actions should run from
	def all_setup_actions(self):
		print(pfx.SUCCESS + "Running Setup...")
		sql_dec.create()

		data = configuration.load_data()
		data["account"]["reset"] = False

		configuration.update_data(data)


class Run(Base):

	def __init__(self):
		super().__init__()
		os.system("clear")
		self.exit_condition = False

		self.load_screen_details()
		self.mainloop()
	
	def mainloop(self):
		prefix = "pwdmn [*] "
		commandHandler = action.Command()
		while not self.exit_condition:
			command_in = input(prefix)
			commandHandler.set_command(command_in)
			commandHandler.handle_command()

			self.exit_condition = commandHandler.exit_condition 

		print("Program exited")




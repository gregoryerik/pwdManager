#!/usr/bin/python3.7
import json
import main
import os
import sys
import tools.prefix as pfx
from tools import configuration 

# Lets the program know if the user forgot to rename the config file
def failedToRenameConfig():
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "default_config.json")
    if os.path.isfile(config_file):
        return True
    return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(sys.argv[1:])
    
    data = configuration.load_data()
    if data is not False:
        first = data["account"]["reset"]
        if first:
            setup = main.Setup()
        else:
            run = main.Run()

    else:
        if failedToRenameConfig():
            print(pfx.WARNING + "You need to rename the default_config.json file to config.json!")
        else:
            messages = ["Could not read the configuration file.", "Default config.json file is not found.", "Download the default configuration json file from GitHub", "https://github.com/gregoryerik/pwdManager/blob/master/default_config.json"]
            for message in messages:
                print(pfx.NOTE + message)
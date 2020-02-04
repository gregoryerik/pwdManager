#!/usr/bin/python3.7
import json
import main
import os
import sys
import tools.prefix as pfx
from tools import configuration 
from tools import action

# Lets the program know if the user forgot to rename the config file
def failedToRenameConfig():
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "default_config.json")
    if os.path.isfile(config_file):
        return True
    return False

def need_setup_mode():
    data = configuration.load_data()
    if data is not False:
        if data["account"]["reset"]:
            return True
        return False
    return None

if __name__ == "__main__":
    
    setup_mode = need_setup_mode()
    single_mode = True if len(sys.argv) > 1 else False


    if setup_mode is not None:
        if setup_mode:
            main.Setup()
        else:
            if single_mode:
                action.SingleAction()
            else:
                main.Run()

    else:
        if failedToRenameConfig():
            print(pfx.WARNING + "You need to rename the default_config.json file to config.json!")
        else:
            messages = ["Could not read the configuration file.", "Default config.json file is not found.", "Download the default configuration json file from GitHub", "https://github.com/gregoryerik/pwdManager/blob/master/default_config.json"]
            for message in messages:
                print(pfx.NOTE + message)
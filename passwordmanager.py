#!/usr/bin/python3.7
import json
import main
import os
import tools.prefix as pfx

def load_data():
    try:
        cwd = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")
        with open(cwd) as json_file:
            data = json.load(json_file)
            return data
    except Exception as e:
        print(e)
        return False

# Lets the program know if the user forgot to rename the config file
def failedToRenameConfig():
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "default_config.json")
    if os.path.isfile(config_file):
        return True
    return False

if __name__ == "__main__":
    data = load_data()
    if data is not False:
        first = data["account"]["first-time"]
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

            manual = input("Manual start? (y/n) ").lower()
            if manual in ["y", "n"]:
                if manual == "y":
                    print("Program paused to allow for editing of configuration file.")
                    input("Press enter when ready to continue.")
                
            else:
                print("That was not what we agreed you would type >:(")
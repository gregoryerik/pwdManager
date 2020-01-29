#!/usr/bin/python3.7
import json
import main
import os

def load_data():
    try:
        cwd = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")
        with open(cwd) as json_file:
            data = json.load(json_file)
            return data
    except Exception as e:
        print(e)
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
        manual = input("Manual start? (y/n) ").lower()
        if manual in ["y", "n"]:
            if manual == "y":
                print("Program paused to allow for editing of configuration file.")
                input("Press enter when ready to continue.")
            
        else:
            print("That was not what we agreed you would type >:(")
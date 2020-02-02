import os
import json

def get_json_file_path():
    return os.path.abspath(os.path.join(__file__, "../../config.json"))

def load_data(failed=None):
    try:
        json_path = get_json_file_path()
        with open(json_path, "r") as json_file:
            data = json.load(json_file)
            return data
    except:
        # When logging is implemented, catch the exception and log it to the file
        if failed is not None:
            print(failed)
        return False

def get_database_path():
    data = load_data()
    file_name = data["database"]["database_name"]
    absolute_path = os.path.abspath(os.path.join(__file__, f"../../storage/{file_name}"))
    return absolute_path

def database_exists():
    return os.path.exists(get_database_path())
    
def update_data(data):
    try:
        json_path = get_json_file_path()
        with open(json_path, "w") as json_file:
            json.dump(data, json_file)
    except:
        print("[!] Can't write to file")

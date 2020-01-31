import os
import json

def load_data(failed=None):
    try:
        json_path = os.path.abspath(os.path.join(__file__, "../../config.json"))
        print(json_path)
        with open(json_path) as json_file:
            data = json.load(json_file)
            return data
    except:
        # When logging is implemented, catch the exception and log it to the file
        if failed is not None:
            print(failed)
        return False
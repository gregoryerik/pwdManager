"""
@author: lightningb4
@date: 09/01/2020

Outputs the password to a QR code in terminal so that a phone can scan
the data for copying to clipboard
"""

import pyqrcode
import os
from PIL import Image

class qrcode:

    def __init__(self, data):
        self.data = data
    
    def create_terminal(self):
        # Basic generation and terminal printing of the qrcode
        code = pyqrcode.create(self.data)
        # the border around the qr code to make the qr code easier to see
        qz = 1
        print(code.terminal(quiet_zone=qz))
    
    def create_open(self):
        # Generating the full path to the image using the relative paths we know
        # And the current working directory as a parent
        relative_path = "../data/qr-code-pwd.png"
        cwd = os.getcwd()
        full_path = os.path.abspath(os.path.join(cwd, relative_path))

        # Creating the PNG image and saving it to the data directory
        # using the pyqrcode <>.show() for png files didnt work so alternative solution
        # has been used <PIL>
        code = pyqrcode.create(self.data)
        code.png(full_path, scale=16)

        # Using PIL to show the image instead of pyqrcode.
        img = Image.open(full_path)
        img.show()

        self.delete_file(full_path)
    
    def delete_file(self, path):
        accepted_answer = False
        while not accepted_answer:
            delete = input("Delete QR code from directory [y/n]? ").lower()
            if delete in ["y", "n"]:
                accepted_answer = True
                if delete == "y":
                    print(f"Deleting the img at path {path}")
                    os.remove(path)
                    print("Deleted.")
                else:
                    contents = [f"Keeping the image stored at {path} for now. Feel free to delete yourself.", 
                    "Please note: the image will be overriden the next time a QR code is generated.",
                    "If you need to keep it then you should rename it or move the file."]
                    for content in contents:
                        print(content)
            else:
                print("Please enter only 'y' or 'n' - no spaces or additional characters.")

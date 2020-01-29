from cryptography.fernet import Fernet
import os
import getpass



class Key:
	
	def __init__(self, location):
		self.location = location
	
	def create(self, name):
		key = Fernet.generate_key()
		try:
			with open(self.location + f"/{name}.key", "wb") as fw:
				fw.write(key)
			print("Saved key sucessfully.")
		except:
			print("Failed to save the key.")

	def get_key(self, name):
		try:
			with open(self.location + f"/{name}.key", "rb") as fr:
				key = fr.read()
			return key
		except:
			return "Err"

def decrypt(pwd, location, name):
	# Decrypt the password with the correct key
	try:
		k = Key(location)
		key = k.get_key(name)
		f = Fernet(key)
		return f.decrypt(pwd)
	except:
		return False

def encrypt(pwd, name):
	# Create new key for each account - name the file after the account
	print("Likely in the /media directory?")
	location = input("Location: ")
	key = Key(location)
	key.create(name)

	f = Fernet(key.get_key(name))
	encrypted = f.encrypt(pwd.encode())
	
	return encrypted


### REMOVE AFTER TESTING

def main():
	## try new key
	pwd = getpass.getpass()
	name = input("Website/Service Name: ")

	encr = encrypt(pwd, name)
	print(encr)

	decr = decrypt(encr, input("Location of key: "), input("Name of key: "))
	if isinstance(decr, bytes):
		print(decr.decode())
	else:
		print("Ran into an issue")

if __name__ == "__main__":
	main()
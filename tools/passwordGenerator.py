import string
import random as r
import pyperclip as clip
from os import system as s
class password:
	""" 
		Base class 
	"""
	def __init__(self):
		""" Variables needed for all child classes """
		self.password = []

	def get(self):
		""" Return the string version of the password """
		if isinstance(self.password, str):
			return self.password
		return "".join(self.password)

class passwordRandom(password):
	"""
		Creates an n-length password of a random combination of characters
	"""
	def __init__(self, length=16):
		""" Create the basic varaibles """
		self.length = length
		self.fullList = self.getFull()


	def getFull(self):
		""" Get the full list of possible characters, filter out any chars that may affect statements """
		full = (string.printable).replace("\"", "")
		full = full.replace("\\", "")
		full = full.replace(" ", "")
		full = full[0:92]
		return full

	def create(self):
		""" Generate the password from the full list of available characters """
		password = []
		for i in range(self.length):
			letter = r.choice(self.fullList)
			password.append(letter)
		self.password = password

class passwordEasy(password):
	"""
		Creates an random password of a random choice of avaiable words and numbers
	"""
	def __init__(self, wordCount=3, numberCount=3):
		""" Create the basic varaibles """
		self.wordCount = wordCount
		self.numberCount = numberCount

	def getWords(self):
		""" Return a set of the 300,000 words in the text file """
		with open('../data/words.txt') as f:
			words = set(f.read().split())
		return words

	def getRandomWords(self):
		""" Return a list of words taken from the file"""
		return r.sample(self.getWords(), self.wordCount)

	def create(self):
		""" Generate the full password from the random words and numbers """
		contents = self.getRandomWords()
		numbers = [i for i in string.digits]

		for i in range(self.numberCount):
			contents.append("".join(r.sample(numbers, 3)))

		r.shuffle(contents)
		password = "_".join(contents)
		self.password = password

if __name__ == "__main__":
	happy = False
	choice = int(input("[1] for Random or [2] for Worded: "))

	if choice in [1,2]:

		if choice == 1:
			p = passwordRandom()
		else:
			p = passwordEasy()

	while not happy:
		p.create()
		print(p.get())

		response = input("Happy with password? [y/n]: ")
		if response.lower() in ['y', 'n']:
			if response.lower() == 'y':
				print("Ok! Copied to clipboard!")
				clip.copy(p.get())
				happy = True
			else:
				s("clear")
				print("Generating new password...\n")
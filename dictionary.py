class Dictionary:
	def __init__(self):
		self.loadDictionary()
		
	def loadDictionary(self):
		with open("guess.txt", encoding = "utf-8") as dictionary:
			self.prediction = \
			[line.strip() for line in dictionary]
		
	def getDictionary(self):
		return self.prediction

class Bruteforcer:
	def __init__(self, password):
		self.password = password
		x = Dictionary()
		self.predictions = x.getDictionary()
	
	def unlockPassword(self):
		for guess in self.predictions:
			if guess == self.password:
				return"guess is {}, password is {}".format(guess, self.password)
		return "your guesses suck"
agent = Bruteforcer("acd")
result = agent.unlockPassword()
print(result)


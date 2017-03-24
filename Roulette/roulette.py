import random
from pick import Pick

class Roulette:
	"""
	Generates pseudo random picks to test algorithms against
	"""

	def next(self):
		"""
		Generates the next Pick
		"""

		choices = [Pick.RED, Pick.BLACK] 	# Define our possibilities
		return random.choice(choices) 		# Pick one at random
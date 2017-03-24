from Roulette.pick import Pick
from algorithm import Algorithm

class AlwaysBlackAlgorithm(Algorithm):
	def guess(self, previous):
		"""
		The logic to determine your guess, given the previous
		"""

		return Pick.BLACK
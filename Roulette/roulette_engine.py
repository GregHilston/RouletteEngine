from pick import Pick
from roulette import Roulette
from algorithm import Algorithm


class RouletteEngine:
	def __init__(self, number_of_rounds_per_run, number_of_runs, algorithm):
		self._number_of_rounds_per_run = number_of_rounds_per_run
		self._number_of_runs = number_of_runs
		self._roulette = Roulette()
		self._algorithm = algorithm


	def start(self):
		total_correct = 0
		prev = Pick.NONE

		for run in range(self._number_of_runs):
			round_correct = 0

			for round in range(self._number_of_rounds_per_run):
				guess = self._algorithm.guess(prev)
				actual = self._roulette.next()

				if(guess == actual):
					round_correct += 1

			print(f"Round {round}: {round_correct} out of {self._number_of_rounds_per_run}")
			total_correct += round_correct
		print(f"Average: {total_correct / self._number_of_runs} out of {self._number_of_rounds_per_run}")
		print(f"Total: {total_correct} out of {self._number_of_runs * self._number_of_rounds_per_run}")

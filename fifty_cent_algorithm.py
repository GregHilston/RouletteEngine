"""As a bonus - you get 50 cent quotes.

Your opinion of yourself becomes your reality.
"""
from Roulette.pick import Pick
from algorithm import Algorithm

class FiftyCentAlgorithm(Algorithm):
    def __init__(self):
        """I love you like a fat kid loves cake."""
        self.red = 0
        self.black = 0

    def guess(self, previous):
        """Always pick what has been picked the least.
           An attempt to get closest to 50/50.
           I’m the type to swallow my blood before I swallow my pride.
        """
        if previous == Pick.NONE:
            return Pick.BLACK

        if previous == Pick.BLACK:
            self.black += 1
        elif previous == Pick.RED:
            self.red += 1
        else:
            raise Exception("Death gotta be easy, ’cause life is hard. It’ll leave you physically, mentally and emotionally scarred.")

        if self.black < self.red:
            return Pick.BLACK
        else:
            return Pick.RED


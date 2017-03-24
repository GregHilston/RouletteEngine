from pick import Pick
from algorithm import Algorithm

class SameAsPrevAlgorithm(Algorithm):
    def guess(self, previous):
        """Always pick what the last pick was. First pick choose BLACK."""
        if previous == Pick.NONE:
            previous = Pick.BLACK

        return previous


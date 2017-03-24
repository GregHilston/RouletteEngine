import sys
from Roulette.roulette_engine import RouletteEngine
from always_black_algorithm import AlwaysBlackAlgorithm
from same_as_prev_algorithm import SameAsPrevAlgorithm
from fifty_cent_algorithm import FiftyCentAlgorithm

def usage():
    sys.exit("usage: $ python3 app.py [number of runs] [number of rounds per runs]")


def main():
    if(len(sys.argv)) != 3:
        usage()

    number_of_runs = int(sys.argv[1])
    number_of_rounds_per_run = int(sys.argv[2])

    always_black_algorithm = AlwaysBlackAlgorithm()
    roulette_engine = RouletteEngine(number_of_runs, number_of_rounds_per_run, always_black_algorithm)
    roulette_engine.start()

    fifty_cent_algorithm = FiftyCentAlgorithm()
    roulette_engine = RouletteEngine(number_of_runs, number_of_rounds_per_run, fifty_cent_algorithm)
    roulette_engine.start()


if __name__ == "__main__":
    main()


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

    algos = [AlwaysBlackAlgorithm(), SameAsPrevAlgorithm(), FiftyCentAlgorithm()]

    for algo in algos:
        RouletteEngine(number_of_runs, number_of_rounds_per_run, algo).start()


if __name__ == "__main__":
    main()


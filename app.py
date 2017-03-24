import sys
sys.path.append("Roulette") # Adds the sub dir so we can import it
from roulette_engine import RouletteEngine
from always_black_algorithm import AlwaysBlackAlgorithm

def main():
	always_black_algorithm = AlwaysBlackAlgorithm()
	roulette_engine = RouletteEngine(3, 3, always_black_algorithm)
	roulette_engine.start()


if __name__ == "__main__":
	main()
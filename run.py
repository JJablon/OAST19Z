import sys

from input_parser import input_parser
from ea import ea
from bfa import bfa


def main():
    # option = input("Select file: net12_1, net12_2, net4\n")
    # if option == "net12_1":
    #     data = input_parser.Parser.read_file("./files/net12_1")
    # elif option == "net12_2":
    #     data = input_parser.Parser.read_file("./files/net12_2")
    # elif option == "net4":
    data = input_parser.Parser.read_file("./files/net12_2")
    # else:
    #     print("exited, wrong_input")
    #     sys.exit()


    # option = input("Do you want run EA? [y/n]: ")
    # if option == "y":
    # seed = input("Seed: ")
    # population_size = input("Population size (Must be even): ")
    # generations = input("Generations: ")
    # mutation_probability = input("Mutation propability: ")
    seed = 7
    population_size = 10  # must be even
    generations = 250
    mutation_probability = 0.05

    links, demands = input_parser.Parser.mp2k(data)
    evo_alg = ea.EvolutionAlgorithm(links, demands, int(seed), int(population_size), int(generations), float(mutation_probability))
    # evo_alg.print()

    # option = input("Do you want run bruteforce? [y/n]: ")
    # if option == "y":
    #     links, demands = input_parser.Parser.mp2k(data)
    #     bruteforce = bfa.BruteForce(links, demands)
    #     bruteforce.solve()


# if __name__ == "__main__":
main()

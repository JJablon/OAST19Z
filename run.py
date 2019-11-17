import sys

from input_parser import input_parser
from ea import ea
from bfa import bfa


def main():
    data = []
    
    option = input("Select file: net12_1, net12_2, net4\n")
    if option == "net12_1":
        data = input_parser.Parser.read_file("./files/net12_1")
    elif option == "net12_2":
        data = input_parser.Parser.read_file("./files/net12_2")
    elif option == "net4":
        data = input_parser.Parser.read_file("./files/net4")
    else:
        print("exited, wrong_input")
        sys.exit()
    
    links, demands = input_parser.Parser.mp2k(data)
    
    option = input("Do you want run EA? [y/n]: ")
    if option == "y":
        seed = 7
        population_size = 10  # must be even
        generations = 20
        mutation_probability = 0.05

        evo_alg = ea.EvolutionAlgorithm(links, demands, seed, population_size, generations, mutation_probability)
        evo_alg.solve()

    option = input("Do you want run bruteforce? [y/n]: ")
    if option == "y":
        bruteforce = bfa.BruteForce(links, demands)
        bruteforce.solve()


if __name__ == "__main__":
    main()

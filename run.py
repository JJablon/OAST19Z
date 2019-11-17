from input_parser import input_parser
from ea import ea2
from bfa import bfa


def main():
    data = input_parser.Parser.read_file("./files/net4")
    links, demands = input_parser.Parser.mp2k(data)

    # option = input("Do you want run bruteforce? [y/n]")
    # if option == "y":
    #     bruteforce = bfa.BruteForce(links, demands)
    #     bruteforce.solve()

    # Probable future  EA call - will rethink it
    evolution = ea2.EvolutionAlgorithm(links, demands, 7, 50, 250, 0.05)
    evolution.solve()


if __name__ == "__main__":
    main()

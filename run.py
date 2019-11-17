from input_parser import input_parser
from ea import ea
from ea import ea2
from bfa import bfa
#for debugging
from pprint import pprint

def main():
    data = input_parser.Parser.read_file("./files/net4")
    links, demands = input_parser.Parser.mp2k(data)

    # ea_sim = ea.EA_simulation(links, demands, 1,1,1,1)
    # pprint(links)

    ea2.EvolutionAlgorithm(links, demands, 1, 2, 0.25)

    #debug:
    # pprint(links)
    # pprint(demands)
    
    # bruteforce = bfa.BruteForce(links, demands)
    # solutions = bruteforce.solve()



if __name__ == "__main__":
    main()

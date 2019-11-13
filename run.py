from input_parser import input_parser
from bfa import bfa
#for debugging
from pprint import pprint

def main():
    data = input_parser.Parser.read_file("./files/net4")
    links, demands = input_parser.Parser.mp2k(data)
    #debug:
    #pprint(links)
    #pprint(demands)
    bruteforce = bfa.BruteForce(links, demands)
    solutions = bruteforce.solve()


if __name__ == "__main__":
    main()

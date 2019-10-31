from input_parser import input_parser
from ea import ea
#for debugging
from pprint import pprint

def main():
    data = input_parser.Parser.read_file("./files/net4")
    links, demands = input_parser.Parser.mp2k(data)
    #debug:
    #pprint(links)
    #pprint(demands)
    ea_sim = ea.EA_simulation(links, demands, 0,1,1,1)



if __name__ == "__main__":
    main()

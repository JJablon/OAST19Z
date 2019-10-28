from parser import parser

def main():
    data = parser.Parser.read_file("./files/net4")
    links, demands = parser.Parser.mp2k(data)

if __name__ == "__main__":
    main()

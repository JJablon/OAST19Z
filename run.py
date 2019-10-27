from parser.parser import Parser

def main():
    data = Parser.read_file("./files/net4")
    links, demands = Parser.mp2k(data)

if __name__ == "__main__":
    main()

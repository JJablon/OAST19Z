from parser.parser import Parser

def main():
    data = Parser.read_file("./files/test")
    print(data)

if __name__ == "__main__":
    main()


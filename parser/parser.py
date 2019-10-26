class Parser:
    def __init__(self):
        pass

    @classmethod
    def read_file(cls, filename):
        data = []
        with open(filename, "r", encoding="UTF-8") as f:
            lines = ''
            for line in f:
                data.append(line.rstrip())
        return data

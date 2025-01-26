def open_file(path):
    with open(path) as f:
        return f.read()
    
MONEY_PATH = "./money.txt"
DOCUMENT = open_file(MONEY_PATH)
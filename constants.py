def get_money_path(path):
    with open(path) as f:
        return f.read()
    
MONEY_PATH = "./money.txt"
DOCUMENT = get_money_path(MONEY_PATH)
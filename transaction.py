class Transaction():
    def __init__(self, amount, name, date):
        self.amount = amount
        self.name = name
        self.date = date


    def print(amount, name, date):
        print(f"{amount}{name}{date}")
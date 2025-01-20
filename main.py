from transaction import *

def main():
    trans1 = Transaction
    trans1.amount = 100
    trans1.name = "groceries"
    trans1.date = "12/2/24"
    print(trans1.amount)
    # main_selection(input("What would you like to do today?\n 1. Withdraw\n 2. Deposit\n 3. View reports\n"))

def main_selection(selection):
    if selection == '1':
        pass
    elif selection == '2':
        pass
    elif selection == '3':
        pass
    else: 
        main_selection(input("Not a valid option\n"))

if __name__ == "__main__":
    main()
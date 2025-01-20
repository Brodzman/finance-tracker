from transaction import *

def main():
    main_selection(input("What would you like to do today?\n 1. Withdraw\n 2. Deposit\n 3. View reports\n"))

def main_selection(selection):
    if selection == '1':
        withdraw_section(input("What account are you withdrawing from?\n 1. Splurge\n 2. Daily Expenses\n 3. Savings\n"))
    elif selection == '2':
        pass # Deposit
    elif selection == '3':
        pass # View reports
    else: 
        main_selection(input("Not a valid option\n"))

def withdraw_section(withdraw_selection):
    if withdraw_selection == '1':
        splurge_category()
    elif withdraw_selection == '2':
        pass # Daily Expenses
    elif withdraw_section == '3':
        pass # Savings

def splurge_category():
    ordered_categories = ''
    catergory_location = 1
    splurge_categories = ['Tech',
                          'Takeaway']
    for category in splurge_categories:
        ordered_categories += ' ' + str(catergory_location) + '. ' + category + '\n'
        catergory_location += 1
    selection_location = int(input(f'Which category?\n{ordered_categories}')) - 1
    
    withdraw_amount = int(input(f'How much would you like to withdraw from {splurge_categories[selection_location]}?\n $'))
    print(withdraw_amount) # Withdraw money

if __name__ == "__main__":
    main()
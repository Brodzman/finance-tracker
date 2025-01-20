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
        daily_expenses_catergory()
    elif withdraw_selection == '3':
        savings_catergory()
    else:
        withdraw_section(input("Not a valid option\n"))
    

def splurge_category():
    ordered_categories = ''
    catergory_location = 1
    # Turn into file
    categories = ['Tech',
                    'Takeaway']
    
    for category in categories:
        ordered_categories += ' ' + str(catergory_location) + '. ' + category + '\n'
        catergory_location += 1
    
    selection_location = int(input(f'Which category?\n{ordered_categories}')) - 1
    withdraw_amount = int(input(f'How much would you like to withdraw from {categories[selection_location]}?\n $'))
    # Withdraw money
    print(withdraw_amount)
    main()

def daily_expenses_catergory():
    ordered_categories = ''
    catergory_location = 1
    # Turn into file
    categories = ['Groceries',
                    'Bills']
    
    for category in categories:
        ordered_categories += ' ' + str(catergory_location) + '. ' + category + '\n'
        catergory_location += 1
    
    selection_location = int(input(f'Which category?\n{ordered_categories}')) - 1
    withdraw_amount = int(input(f'How much would you like to withdraw from {categories[selection_location]}?\n $'))
    # Withdraw money
    print(withdraw_amount)

def savings_catergory():
    ordered_categories = ''
    catergory_location = 1
    # Turn into file
    categories = ['Stocks',
                    'Running out of money']
    
    for category in categories:
        ordered_categories += ' ' + str(catergory_location) + '. ' + category + '\n'
        catergory_location += 1
    
    selection_location = int(input(f'Which category?\n{ordered_categories}')) - 1
    withdraw_amount = int(input(f'How much would you like to withdraw from {categories[selection_location]}?\n $'))
    # Withdraw money
    print(withdraw_amount)



if __name__ == "__main__":
    main()
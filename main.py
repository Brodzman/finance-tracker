from transaction import *
from constants import *

def main():
    print(DOCUMENT)
    main_selection(input("What would you like to do today?\n 1. Withdraw\n 2. Deposit\n 3. View reports\n"))

def main_selection(selection):
    if selection == '1':
        withdraw_section(input("What account are you withdrawing from?\n 1. Splurge\n 2. Daily Expenses\n 3. Savings\n"))
    elif selection == '2':
        deposit_section(input("What account would you like to deposit to?\n 1. Splurge\n 2. Daily Expenses\n 3. Savings\n 4. Apply Bucket Rule\n"))
    elif selection == '3':
        pass # View reports
    else: 
        main_selection(input("Not a valid option\n"))

# WITHDRAW
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
    withdraw_amount = int(input(f'How much would you like to withdraw from {categories[selection_location]}?\n$'))
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
    withdraw_amount = int(input(f'How much would you like to withdraw from {categories[selection_location]}?\n$'))
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
    withdraw_amount = int(input(f'How much would you like to withdraw from {categories[selection_location]}?\n$'))
    # Withdraw money
    print(withdraw_amount)

# Copy of main selection
#
# def main_selection(selection):
#     if selection == '1':
#         withdraw_section(input("What account are you withdrawing from?\n 1. Splurge\n 2. Daily Expenses\n 3. Savings\n"))
#     elif selection == '2':
#         pass # Deposit
#     elif selection == '3':
#         pass # View reports
#     else: 
#         main_selection(input("Not a valid option\n"))

def deposit_section(deposit_selection):
    if deposit_selection == '1':
        print(input('How much would you like to deposit to Splurge?\n'))
    elif deposit_selection == '2':
        pass # Daily exp
    elif deposit_selection == '3':
        pass # Savings
    elif deposit_selection == '4':
        bucket_section(input("Which bucket system would you like to use?\n 1. Base (10, 30, 60)\n 2. Custom"))
    else:
        deposit_section(input("Not a valid option\n"))

def bucket_section(bucket_type):
    if bucket_type == '1':
        pass





if __name__ == "__main__":
    main()
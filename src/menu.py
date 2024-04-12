
import sys
import os
import time

from data_parser import read_dataset, write_dataset

EVASIVE_FILE = '../dataset2/evasive.csv'
NON_EVASIVE_FILE = '../dataset2/non_evasive.csv'

#################### Auxiliar Functions ######################

# Clear screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
# Exit Menu Function
def exit_application():
    print("Exiting the application. Goodbye!")
    sys.exit()

# Input Handling Function
def error_handling_input():
    print("Invalid option.")
    input("Press Enter to continue...")
    menu()

#################### Main Functions ######################

def data_set_menu(evasive, non_evasive):
    clear_screen()
    write_dataset(evasive, non_evasive)
    input("Press Enter to continue...")
    menu()




def menu():
    clear_screen()

    # Read stuff
    evasive = read_dataset(EVASIVE_FILE)
    non_evasive = read_dataset(NON_EVASIVE_FILE)


    # Print Init UI
    print("--------------------------------------------------------------------------------")
    print("Welcome to our application")
    print("--------------------------------------------------------------------------------")
    print("What do you want to do:")
    print("1. See Dataset")
    print("0. Exit")
    print("--------------------------------------------------------------------------------")
    
    choice = input("Please enter your choice: ")

    options = {
        '1': data_set_menu(evasive, non_evasive),
        '0': exit_application
    }

    selected_option = options.get(choice)

    if selected_option:
        selected_option()
    else:
        error_handling_input()

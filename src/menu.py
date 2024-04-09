
import sys
import os
import time


INPUT_FILE = '../database/...'

#################### Auxiliar Functions ######################

# Clear screen
def clear_screen():
    os.system('cls')        ## if windows 
    ## os.system('clear')   ## if linux/macs

# Exit Menu Function
def exit_application():
    print("Exiting the application. Goodbye!")
    sys.exit()

# Input Handling Function
def error_handling_input():
    print("Invalid option.")
    input("Press Enter to continue...")
    return menu()

#################### Main Functions ######################

def menu1():
    clear_screen()
    print("Ola 1 :)")


def menu2():
    clear_screen()
    print("Ola 2 :)")



def menu():
    clear_screen()

   # Print Init UI
    print("--------------------------------------------------------------------------------")
    print("Welcome to our application")
    print("--------------------------------------------------------------------------------")
    print("What do you want to do:")
    print("1. See feature 1")
    print("2. See feature 2")
    print("0. Exit")
    print("--------------------------------------------------------------------------------")
    
    choice = input("Please enter your choice: ")

    options = {
        '1': menu1,
        '2': menu2,
        '0': exit_application
    }

    selected_option = options.get(choice)

    if selected_option:
        selected_option()
    else:
        print("Invalid choice. Please enter a valid option.")
        input("Press Enter to continue...")
        menu()
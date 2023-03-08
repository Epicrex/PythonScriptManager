"""
PSM = Python Script Manager
Author: Sidney
Created: 2022
Agreement type: ... (Open Source)

All the rights to this code are owned fully by it's author.

---

ToDo: Switch current default print to my custom user input lib
"""

from colorama import Fore, Back, Style

from lib_manager import lib_console_styling as style
from lib_manager import lib_user_input as inp
from lib_manager import lib_psm_vars_for_main as main_var
from lib_back_or_exit import trigger_back_or_exit_action


# Description for user
print("----------------------------------------\n")
print("\x1B[3mAll the rights to this code are owned fully by it's author, Sidney\n")
style.description("\x1B[0m", "Hi ...", "")

# Infinitely loop until user is done
while "2B" or not "2B":

    # Info on what to do for user
    print(f"\nPlease chose one of the following scripts by inputting it's corresponding{Fore.BLUE}{Style.BRIGHT} number: \n{Style.RESET_ALL}")

    # Python Script List
    for script in main_var.allScriptsList:
        print(f'{Fore.BLUE}{Style.BRIGHT}{script[0]}{Style.RESET_ALL}: {script[2]}')

    # Waiting message
    style.waiting("", "Waiting for input...", "")

    # Get User Input
    user_input = input()
    if trigger_back_or_exit_action(user_input):
        style.error("", "Already top level of PSM, no where to go back to.", "")
    else:

        # Error
        if user_input == "" or not user_input.isnumeric():
            style.error("", "Please enter a number.", "")

        # Call Python Scripts
        else:
            scriptFlag = False
            for script in main_var.allScriptsList:
                if int(user_input) == script[0]:
                    style.description("\n\n", script[3], "\n")
                    script[1]()
                    scriptFlag = True
            # Further errors
            if not scriptFlag:
                style.error("", "Please enter a valid number.", "")

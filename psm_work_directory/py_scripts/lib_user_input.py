import lib_console_styling as style
from lib_back_or_exit import back_list
from lib_back_or_exit import exit_list


#####################################################################################
# Raw
#####################################################################################
def raw_input():
    user_input = get_user_input()

    if user_input in back_list:
        return "back"
    elif user_input in exit_list:
        return "exit"
    else:
        return user_input


#####################################################################################
# String
#####################################################################################
def string_input():
    user_input = get_user_input()
    user_input = and_sanitise_user_input(user_input)

    user_input = str(user_input)

    if user_input in back_list:
        return "back"
    elif user_input in exit_list:
        return "exit"
    else:
        return user_input


#####################################################################################
# Number
#####################################################################################
def number_input():
    user_input = get_user_input()
    user_input = and_sanitise_user_input(user_input)

    if user_input.isdecimal():
        user_input = int(user_input)
    else:
        style.error("\n", "Invalid input", "")
        style.waiting("", "Please enter a number (without decimals)...", "")

    if user_input in back_list:
        return "back"
    elif user_input in exit_list:
        return "exit"
    else:
        return user_input


#####################################################################################
# Float
#####################################################################################
def decimal_input():
    user_input = get_user_input()
    user_input = and_sanitise_user_input(user_input)

    if user_input.isdecimal():
        user_input = float(user_input)

    else:
        style.error("\n", "Invalid input", "")
        style.waiting("", "Please enter a number (can have decimals)...", "")

    if user_input in back_list:
        return "back"
    elif user_input in exit_list:
        return "exit"
    else:
        return user_input


#####################################################################################
# Util
#####################################################################################
def get_user_input():
    user_input = input()
    user_input = user_input.strip()
    return user_input


def and_sanitise_user_input(user_input):
    user_input = user_input.strip()
    return user_input

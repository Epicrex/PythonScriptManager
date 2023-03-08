"""
Helps print with color.

For descriptions use (purple) -> print_description("OPTIONAL_SUFFIX", "PRINT_STRING", "OPTIONAL_PREFIX")
For waiting use (yellow) -> print_waiting("OPTIONAL_SUFFIX", "PRINT_STRING", "OPTIONAL_PREFIX")
For errors use (red) -> print_error("OPTIONAL_SUFFIX", "PRINT_STRING", "OPTIONAL_PREFIX")
For success use (green) -> print_success("OPTIONAL_SUFFIX", "PRINT_STRING", "OPTIONAL_PREFIX")

If you don't want to use all 3 parameters pass the string but keep it empty like this: print_success("", "yay", "")
"""
import colorama.initialise
from colorama import Fore, Back, Style

colorama.initialise.init(convert=True)
reset = Style.RESET_ALL


def normal(optional_suffix, print_string, optional_prefix):
    print(optional_suffix + print_string + optional_prefix)


def description(optional_suffix, print_string, optional_prefix):
    print(optional_suffix + Fore.MAGENTA + Style.BRIGHT + print_string + reset + optional_prefix)


def waiting(optional_suffix, print_string, optional_prefix):
    print(optional_suffix + Fore.YELLOW + Style.BRIGHT + print_string + reset + optional_prefix)


def error(optional_suffix, print_string, optional_prefix):
    print(optional_suffix + Fore.RED + Style.BRIGHT + "[ERROR] " + print_string + reset + optional_prefix)


def success(optional_suffix, print_string, optional_prefix):
    print(optional_suffix + Fore.GREEN + Style.BRIGHT + print_string + reset + optional_prefix)


def highlight(optional_suffix, print_string, optional_prefix):
    print(optional_suffix + Fore.BLUE + Style.BRIGHT + print_string + reset + optional_prefix)

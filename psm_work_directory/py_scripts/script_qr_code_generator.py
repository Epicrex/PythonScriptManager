import qrcode
import os
#import wifi_qrcode
from lib_manager import lib_console_styling as style
from lib_manager import lib_user_input as inp
from colorama import Fore, Back, Style
from lib_back_or_exit import trigger_back_or_exit_action

about_qr_codes = f"""
===========================================================
~~~ What does QR stand for ~~~\n
It stands for "Quick Response code"\n
~~~ Finder Pattern ~~~\n
QR codes have "finder pattern" blocks in 3 of the 4 corners,\nthese are used for orientation.\n
~~~ Quiet Zone ~~~\n
This is the empty white border around the outside of a QR code.\nWithout this border, a QR reader will not be able to determine,\nwhat is and isn't contained within the QR code\n(due to interference from outside elements).\n
~~~ ECC Levels ~~~\n
QR codes can be one of 4 ECC levels:\nL, M, Q, H.\n\nThese determine how much of the QR code can be covered or damaged:\nL:7%, M:15%, Q:25%, H:30%.\n\nECC stands for Error Correction Code.\n
~~~ Module ~~~\n
Modules refer to every black and white square in the QR code.\n
~~~ Versions ~~~\n
There are 40 QR code versions.\nThese versions indicate the size (number of modules) in QR code.\n(More info to every version here: https://www.qrcode.com/en/about/version.html)\n
~~~ QR Code Storage Capabilities ~~~\n
Version 1 QR codes are:\n
  - 21x21\n
  - Able to store 25 Alphanumeric characters with ECC level L\n
  - Or 10 Kanji with ECC level L\n
Version 40 QR codes:\n
  - 177x177\n
  - Able to store 4,296 Alphanumeric characters with ECC level L\n
  - Or 1,817 Kanji with ECC level L
===========================================================
"""


def main():
    i = 1
    print_intro()
    while "2B" or not "2B":
        # User Input
        print_waiting_for_input()
        user_input = get_user_input()
        # Check to go back or leave
        if trigger_back_or_exit_action(user_input):
            print("\n")
            return
        # More about QR codes
        if user_input.lower() == "qr info" or user_input.lower() == "\"qr info\"":
            print_more_about_qr_codes()
            continue
        # Create and Save QR code
        qr, file_name, file_extension = create_qr_code(i, user_input)
        qr_code_name = save_qr_code(i, qr, file_name, file_extension)
        print_qr_code_saved(qr_code_name)


def print_intro():
    print(f"Enter a {Fore.BLUE}{Style.BRIGHT}text/ URL{Style.RESET_ALL} or the words {Fore.BLUE}{Style.BRIGHT}\"qr info\"{Style.RESET_ALL}, if you want to know more about how QR codes work.")


def print_waiting_for_input():
    style.waiting("", "Waiting for input...", "")


def print_qr_code_saved(qr_code_name):
    style.success("", f"QR code \"{qr_code_name}\" successfully created.", "\n")


def print_more_about_qr_codes():
    style.normal("", about_qr_codes, "")


def get_user_input():
    return inp.string_input()


def create_qr_code(i, user_input):
    file_name = "qr_code_"
    file_extension = ".png"

    while os.path.exists(f"{file_name}{i}{file_extension}"):
        i += 1

    qr = qrcode.QRCode()
    qr.add_data(user_input)
    qr.make(fit=True)

    return qr, file_name, file_extension


def save_qr_code(i, qr, file_name, file_extension):
    # Check if the file already exists
    full_file_name = f"{file_name}{i}{file_extension}"
    while os.path.exists(full_file_name):
        i += 1
        full_file_name = f"{file_name}{i}{file_extension}"

    # Save the QR code
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(full_file_name)

    return full_file_name

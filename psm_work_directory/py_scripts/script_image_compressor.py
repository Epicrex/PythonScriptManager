"""
Resources:
https://www.thepythoncode.com/article/compress-images-in-python
https://pillow.readthedocs.io/en/stable/reference/Image.html
https://www.tutorialspoint.com/python_pillow/python_pillow_quick_guide.htm
"""

import PIL
from PIL import Image
from tkinter.filedialog import *  # For file explorer
from colorama import Fore, Back, Style

from lib_manager import lib_console_styling as style
from lib_manager import lib_user_input as inp
from lib_back_or_exit import trigger_back_or_exit_action


#####################################################################################
# Get User Input
#####################################################################################
def main(compression_ratio=0.7, compression_quality=30, width=100, height=100, to_jpg=True):

    compression_mode = 0  # COMPRESSION MODE
    compression_mode_predefined_list = [1, 2]
    # Check if compress mode 1 or 2 is chosen
    
    continue_flag = True
    skip_settings = False

    while continue_flag:
        while compression_mode not in compression_mode_predefined_list and not skip_settings:
            print("Please choose between the following by typing the corresponding "+Fore.BLUE+Style.BRIGHT+"number"+Style.RESET_ALL+":\n\n"+Fore.BLUE + Style.BRIGHT+"1"+Style.RESET_ALL+": Reduce image size by ratio" +Fore.BLUE + Style.BRIGHT+" (recommended)\n2"+Style.RESET_ALL+": Reduce image size to custom height/ width")
            style.waiting("", "Waiting for input...", "")
            compression_mode = inp.number_input()
            # If compression mode 1
            if compression_mode == 1:
                compression_ratio = 0  # COMPRESSION RATIO
                # Check if size ratio input is valid (valid: 0.1 - 1)
                while compression_ratio <= 0 or compression_ratio > 1:
                    print("\nPlease enter the "+Fore.BLUE+Style.BRIGHT+"RATIO"+Style.RESET_ALL+". \x1B[3mExample: 0.7")
                    style.waiting("\x1B[0m", "Waiting for input...", "")
                    compression_ratio = inp.decimal_input()
                    # Print error for when size ratio is false
                    if compression_ratio <= 0 or compression_ratio > 1:
                        print("\nInput number needs to be between 0.1 and 1")
            # If compression mode 2
            elif compression_mode == 2:
                new_width = 0  # HEIGHT
                new_height = 0  # WIDTH
                while new_width <= 0 or new_height <= 0:
                    print("Please enter the width and height, starting with WIDTH. Example: 350")
                    new_width = inp.number_input()
                    new_height = inp.number_input()
                    print("Now enter the HEIGHT. Example: 120")
                    if new_width <= 0 or new_height <= 0 or new_height <= 0 or new_height <= 0:
                        print("Width and height must be greater than 0")
                        
            # If compression mode incorrect
            else:
                print("Invalid input.")

        compression_quality = 0  # compression_quality
        # Check if compression_quality input is valid (valid: 0 - 100)
        while (compression_quality <= 0 or compression_quality > 100) and not skip_settings:
            print("\nPlease enter the the compression "+Fore.BLUE+Style.BRIGHT+"QUALITY"+Style.RESET_ALL+". \x1B[3mExample: 75")
            style.waiting("\x1B[0m", "Waiting for input...", "")
            compression_quality = inp.number_input()
            if compression_quality <= 0 or compression_quality > 100:
                print("Quality needs to be between 1 and 100")
                
        
#####################################################################################
# Compress Image
#####################################################################################
        # Get all image paths
        image_path_list = askopenfilenames()
        # print (image_path_list)
        
        # Enumerate though image list
        try:
            for image_path in image_path_list:
                # Open every image from list
                img = Image.open(image_path).convert("RGB")
                # print(img.size)
                # print(img.info)
                pass
                # Change image ratio
                if compression_ratio != 0:     
                    resized_image = img.resize((int(img.size[0] * compression_ratio), int(img.size[1] * compression_ratio)), PIL.Image.Resampling.LANCZOS)
                # If ratio isn't set change image width and height
                else:
                    resized_image = img.resize((int(width), (int(height))), PIL.Image.Resampling.LANCZOS)

                # Get new name Prep
                new_filename = image_path.rsplit("/", 1)[1]
                # New file extension        
                if to_jpg:
                    new_extension = "jpg"
                else: 
                    new_extension = new_filename.rsplit(".", 1)[1]
                # New file name
                new_filename = new_filename.rsplit(".", 1)[0]

                # Save
                resized_image.save(new_filename + "_compressed" + "." + new_extension, quality=compression_quality, optimize=True)
        except:
            style.error("\n", "Something went wrong with the compression...", "")
        
        # Compression Success message for one image
        if len(image_path_list) == 1:
            style.success("\n", "The Image was successfully compressed with the suffix \"_compressed\"", "")
        # Compression Success message for multiple images
        else:
            style.success("\n", "The Images where successfully compressed with the suffix \"_compressed\"", "")

        post_compression_selection_flag = True
        while post_compression_selection_flag:
            print("\nHow would you like to continue:\n1: Continue Compressing Images with the current profile\n2: Compress another image and re enter the compression settings\n3: Go back to script selection")
            
            post_compression_selection = inp.number_input()
            
            if post_compression_selection == 1:
                post_compression_selection_flag = False
                skip_settings = True
                
            elif post_compression_selection == 2:
                post_compression_selection_flag = False
                skip_settings = False
                
                # Resetting vars
                compression_mode = 0
                compression_ratio = 0
                new_width = 0
                new_height = 0
                compression_quality = 0
                
                # To correct gap
                print("")
                
            elif post_compression_selection == 3:
                post_compression_selection_flag = False
                continue_flag = False
            else:
                style.error("", "Please enter one of the given numbers", "")

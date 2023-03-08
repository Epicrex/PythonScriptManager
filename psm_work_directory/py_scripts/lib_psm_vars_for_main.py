from script_ping import main as script_ping_main
from script_yt_video_downloader import main as script_yt_video_downloader_main
from script_projects_to_do import main as script_projects_to_do_main
from script_image_compressor import main as script_image_compressor_main
from script_qr_code_generator import main as script_qr_code_generator_main

"""
[ID_OF_SCRIPT (integer),
 NAME_OF_SCRIPT (string),
  SHORT_DESCRIPTION_OF_SCRIPT (string),
   LONG_DESCRIPTION_OF_SCRIPT (string)]
"""
allScriptsList = [[0, script_projects_to_do_main, "Scripts on the horizon", "These are the ideas in my backload which may be added to PSM in the future, only time will tell."],
                  [1, script_yt_video_downloader_main, "Download YouTube video", "Downloads the highest resolution video with sound using a YouTube url.\nSadly doesn't work for YT Music links as far as I know."],
                  [2, script_ping_main, "Ping Google", "This is the ping script.."],
                  [3, script_image_compressor_main, "Compress image", "This script will compress any image.\nImportant things to know about this script:\n- Will Convert the color profile to RGB, thus losing alpha.\n\n!Note that this script has not yet been made full proof to errors yet!"],
                  [4, script_qr_code_generator_main, "Generate QR code", "Generates a QR code using a text or URL."]]

from lib_manager import lib_console_styling as style

projects_to_do_list = ["Image/ Video Upscaler",
                       "Video Trim Tool",
                       "Url Shortener",
                       "Download videos form social media platforms",
                       "Get Special Spotify Info",
                       "Get info on devises in network",
                       "Get Info on current device",
                       "Get info on devices connected to current device",
                       "Zip Password Cracker",
                       "My Socials",
                       "Vulnerability Check",
                       "Video to Text,"
                       "Check for email leak"]


""" More info on projects
Get Info on current device: Public IP, Private IP, Public MAC, Private MAC, device name(s), current user(name, rights, ...), os and version, maybe hardware?
Generate QR Code: Generate QR Code from links, images and files
"""


def main():
    print("\n===========================================================")
    print("\nThese are the projects I'm planning on adding to this script manager:\n")
    for item in projects_to_do_list:
        print("- "+item)
    print("\n===========================================================")

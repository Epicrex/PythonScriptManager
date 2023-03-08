import platform
import subprocess  # For executing a shell command
from hashlib import new
from socket import if_indextoname  # For getting the operating system name

from lib_manager import lib_console_styling as style
from lib_manager import lib_user_input as inp


host = "google.com"


def main():

    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = "-n" if platform.system().lower() == "windows" else "-c"

    # Building the command. Ex: "ping -c 1 google.com"
    command = ["ping", param, "6", host]

    # The pinging and the ping result
    print("\n===========================================================")
    subprocess.call(command) == 0
    print("\n===========================================================")

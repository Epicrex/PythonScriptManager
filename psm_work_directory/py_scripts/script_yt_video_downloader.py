"""
Author: Sidney
Created: 2022
PyTube Repo: https://github.com/pytube/pytube
Install Requirements: python -m pip install pytube

How To Use: This script downloads the highest resolution video from the inputted url.
Run the py script by typing "py GetYTVideo.py" into a console window on the same folder level.
Then after prompt enter the url.

ToDo: let user switch to yt dll which most likely can get higher quality
"""
from pytube import YouTube
from colorama import Fore, Back, Style
from sre_constants import SUCCESS
import re
import os

from lib_manager import lib_console_styling as style
from lib_manager import lib_user_input as inp
from lib_back_or_exit import trigger_back_or_exit_action
from lib_back_or_exit import back_list
from lib_back_or_exit import exit_list


def main():
    while "2B" or not "2B":

        print_ask_for_url()
        video_url = get_url_from_user()
        if trigger_back_or_exit_action(video_url):
            print("\n")
            return
        video_downloader_id = choosing_the_downloader()
        if trigger_back_or_exit_action(video_downloader_id):
            print("\n")
            return

        if video_downloader_id == "1" or video_downloader_id == "":
            download_video_with_pytube(video_url)
        elif video_downloader_id == "2":
            download_video_with_youtubedll(video_url)


def print_ask_for_url():
    style.waiting("", "Please enter a video URL...", "")


def get_url_from_user():
    video_url = ""
    while not video_url:
        video_url = input()
        #video_url = inp.raw_input()
        #print_error(video_url)
        return video_url


def print_error(video_url):
    error_happened = False
    error_happened = error_url_is_empty(video_url, error_happened)
    error_happened = error_something_else_is_wrong_with_the_url(video_url, error_happened)


def error_url_is_empty(video_url, error_happened):
    if not error_happened and not video_url:
        style.error("", "URL is empty.", "")
        style.waiting("\n", "Please enter a video URL...", "")
        error_happened = True
        return error_happened


def error_something_else_is_wrong_with_the_url(video_url, error_happened):
    if not error_happened and "https://www.youtube.com/" not in video_url:
        style.error("\n", "Something is wrong with the URL.", "")
        style.waiting("", "Please enter a correct video URL...", "")
        error_happened = True
        return error_happened


def choosing_the_downloader():
    video_downloader_id = "0"
    valid_video_downloader_ids = ["", "1", "2"]

    while video_downloader_id not in valid_video_downloader_ids and video_downloader_id not in back_list and video_downloader_id not in exit_list:
        style.normal("", f"\nPlease chose one of the following downloaders by inputting it's corresponding {Fore.BLUE}{Style.BRIGHT}number{Style.RESET_ALL}:", "")  # make number blue
        style.normal("", f"{Fore.BLUE}{Style.BRIGHT}1{Style.RESET_ALL}: PyTube (default)\n{Fore.BLUE}{Style.BRIGHT}2{Style.RESET_ALL}: YoutubeDLL (not yet implemented)", "")
        style.waiting("", "Waiting for choice ...", "")

        video_downloader_id = input()
        #video_downloader = inp.number_input()

        if video_downloader_id not in valid_video_downloader_ids and video_downloader_id not in back_list and video_downloader_id not in exit_list:
            style.error("", "No downloader with that number.", "")

    return video_downloader_id


#########################################################################
# PYTUBE
#########################################################################
def download_video_with_pytube(video_url):
    urls = handle_multiple_urls(video_url)
    print_waiting_for_download_to_finish(urls)
    try:
        for url in urls:
            video = YouTube(url)
            video = video.streams.get_highest_resolution()
            video_name = video.download()
            print_successfully_downloaded_video(video_name)

    except:
        print_video_download_failed()


def handle_multiple_urls(video_url):
    return re.findall(r'https?://\S+', video_url)


#########################################################################
# YOUTUBEDLL
#########################################################################
def download_video_with_youtubedll(video_url):
    print_waiting_for_download_to_finish()
    try:
        # ToDo: Youtube Dll video downloader
        pass

    except:
        print_video_download_failed()


#########################################################################
# Reused methods for all downloaders
#########################################################################
def print_waiting_for_download_to_finish(urls):
    amount_of_urls = len(urls)
    if amount_of_urls == 1:
        style.waiting("\n", f"... downloading {amount_of_urls} video, please wait ...", "")

    else:
        style.waiting("\n", f"... downloading {amount_of_urls} videos, please wait ...", "")


def print_successfully_downloaded_video(video_name):
    video_name = os.path.basename(video_name)
    style.success("", f"Video \"{video_name}\" successfully downloaded.", "\n")


def print_video_download_failed():
    style.error("\n", "The download failed either because of the URL, internet connection, network/ proxy settings or something else host/  client related", "")

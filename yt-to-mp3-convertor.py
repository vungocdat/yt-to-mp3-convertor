# Program will take YouTube url (in "") as an argument. Then take the link and download a video from the address.
# after downloading it will convert the video into mp3 file and clean after the conversion (delete mp4 file)
# The program is made for macOS and Linux
import sys
import pytube
import os
from pydub import AudioSegment
from sys import argv

# Variables
directory = "audio"     # name of the directory where mp3 files will be stored


def download_yt_video(url):
    """
    Download a YouTube video with the highest resolution
    """
    video = pytube.YouTube(url)
    high_quality_video = video.streams.get_highest_resolution()
    high_quality_video.download()


def convert_to_mp3(filename):
    """
    Convert downloaded video to mp3
    """
    audio = AudioSegment.from_file(filename)
    audio.export(f"{os.path.splitext(filename)[0]}.mp3", format="mp3")     # take the path of thr file and drop mp4


def cleanup(mp3, mp4):
    """
    remove mp4 file and move mo3 file to a directory to keep it clean
    """
    os.remove(mp4)  # cleanup - removes downloaded video to keep just mp3 file
    os.replace(mp3, f"{directory}/{mp3}")


def search_in_current_directory(prefix):
    for i in os.listdir():
        if prefix in i:
            file_name = i
            return file_name


if __name__ == "__main__":
    if len(argv) < 2:
        sys.exit("You need to enter YouTube URL address of the video.")

    if not os.path.exists(directory):
        os.mkdir(directory)

    # link = 'https://www.youtube.com/watch?v=6ZBkDISjv2c&list=LL&index=28'
    link = argv[1]

    download_yt_video(link)
    mp4_file = search_in_current_directory(".mp4")

    convert_to_mp3(mp4_file)
    mp3_file = search_in_current_directory(".mp3")
    cleanup(mp3_file, mp4_file)

    print("Converting is done!")
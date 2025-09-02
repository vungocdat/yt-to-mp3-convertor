# Program will take YouTube URL address and then download the video.
# after downloading it will convert the video into mp3 file and clean
# after the conversion (delete mp4 file)

from pytubefix import YouTube
import os
from pydub import AudioSegment

# Variables
directory = "audio"     # name of the directory where mp3 files will be stored


def download_yt_video(url):
    """
    Download a YouTube video with the highest resolution
    """
    print("Downloading video . . .")
    yt = YouTube(url)
    high_quality_video = yt.streams.get_highest_resolution()
    high_quality_video.download()
    print("Youtube video downloaded.\n")


def convert_to_mp3(filename):
    """
    Convert downloaded video to mp3
    """
    print("Converting video . . .")
    audio = AudioSegment.from_file(filename)
    # take the path of thr file and drop mp4
    audio.export(f"{os.path.splitext(filename)[0]}.mp3", format="mp3")
    print("Converting finished.\n")


def cleanup(mp3, mp4):
    """
    remove mp4 file and move mo3 file to a directory to keep it clean
    """
    print("Performing cleanup . . .")
    os.remove(mp4)  # cleanup - removes downloaded video to keep just mp3 file
    os.replace(mp3, f"{directory}/{mp3}")
    print("Cleanup done.\n")


def search_in_current_directory(prefix):
    """
    Fuction returns the full name of the mp4 file.
    It was created because some file may have spaces and special characters
    """
    for i in os.listdir():
        if prefix in i:
            file_name = i
            return file_name


if __name__ == "__main__":
    # if the directory does not exists then create one
    if not os.path.exists(directory):
        os.mkdir(directory)

    link = input("Enter the URL of Youtube video: ")

    download_yt_video(link)
    mp4_file = search_in_current_directory(".mp4")

    convert_to_mp3(mp4_file)
    mp3_file = search_in_current_directory(".mp3")
    cleanup(mp3_file, mp4_file)

    print("THE PROCESS HAS FINISHED SUCCESSFULLY!")

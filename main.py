# Program will take YouTube url (in "") as an argument. Then take the link and download a video from the address.
# after downloading it will convert the video into mp3 file and clean after the conversion (delete mp4 file)

import pytube
import os
from pydub import AudioSegment

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


if __name__ == "__main__":
    if not os.path.exists(directory):
        os.mkdir(directory)
    link = 'https://www.youtube.com/watch?v=hLu9KghP7Rs&list=LL&index=33'
    mp4_file = f"{pytube.YouTube(link).title}.mp4"
    mp3_file = f"{pytube.YouTube(link).title}.mp3"
    download_yt_video(link)
    convert_to_mp3(mp4_file)      # name of the downloaded video with .mp4 at the end
    cleanup(mp3_file, mp4_file)

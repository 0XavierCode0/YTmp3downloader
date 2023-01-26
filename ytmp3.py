from pytube import YouTube
from pytube import Playlist
from pytube import streams
import os
import glob
import shutil
from moviepy.editor import *


#Downloads Mp4 audio of a song or a playlist from Youtube.
#Converts songs to Mp3 and then deletes mp4
#Moves mp3 to Music

def DLPLaylist(url):
    p = Playlist(url)
    print(f'Downloading: {p.title}')
    for video in p.videos:
        try:
            video.streams.get_audio_only().download()
            print(f"{video.title} downloaded")
        except:
            print(f"Error downloading {video.title}")


def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_audio_only()
    try:
        youtubeObject.download()
    except:
        print("Error downloading")
    print("Download complete!")


def converttomp3():
    files = glob.glob("C:\\Users\\X\\PycharmProjects\\YTdownloader\\*.mp4")

    for file in files:
        directory, song = file.split("YTdownloader\\")
        audioclip = AudioFileClip(file)
        song_title, mp4 = song.split(".")
        audioclip.write_audiofile(f'{song_title}.mp3')
        audioclip.close()
        os.remove(file)
        print("mp3 made and mp4 deleted")


def move_mp3s():

    mp3s = glob.glob("C:\\Users\\X\\PycharmProjects\\YTdownloader\\*.mp3")
    dest = "C:\\Users\\X\\Music"

    for mp3 in mp3s:
        try:
            shutil.move(mp3, dest)
            path, song_name = mp3.split("YTdownloader\\")
            print(f"{song_name} successfully moved to Music")
        except:
            print(f'Error moving {song_name}. Song may already exist')
            continue


DL_Function = input("Download Song or Playlist? ")
if DL_Function == 'Song':
    link = input("YT link here: ")
    Download(link)


if DL_Function == 'Playlist':
    url = input('Playlist URL: ')
    DLPLaylist(url)

converttomp3()
move_mp3s()

print("All done")

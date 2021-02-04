#!/usr/bin/env python3

# ---------------------------------------------
# ---			 Yata Garasu 				---
# ---------------------------------------------
#
# YouTube Downloading Skript that allows to download every video in the given Playlists as mp4, convert them to mp3 files and set the metadata


import sys
import os
import eyed3
from moviepy.editor import *
from pytube import YouTube
from pytube import Playlist


# Change in the correct dir
os.chdir('Lost Sounds')

# Set Playlist URLs in List data structure
Playlist_List = [
"https://www.youtube.com/playlist?list=PLwKVIFPT-TjlwnTdvM4pU22MYey6zucuz", 
"https://www.youtube.com/playlist?list=PLwKVIFPT-TjmHGrGRaxIt8kkfNH6dWNBY", 
"https://www.youtube.com/playlist?list=PLwKVIFPT-Tjk63NsS8WUg_UJKEE-_3zfR"
]

print ("Starting Downloading Skript ...\n")

# Iterating through the List of Playlists defined above
for j in range(len(Playlist_List)):
    yt_pl = Playlist(Playlist_List[j])

    # Calculate the Count of the Videos
    count = 0
    for i in range(len(yt_pl.video_urls)):
        count = count + 1
        
    print("Downloading Playlist:", yt_pl.title, "[", count, " Elements] \n")

    for video in yt_pl.videos:
        # Downloading every video in the playlist
        print("Downloading:", video.title)
        video.streams.first().download(output_path=yt_pl.title, skip_existing=True)
        
    print("\nFinished downloading Playlist,", yt_pl.title)
    print("-------------------------------------------------------------\n")


########################################################################################


print ("Starting Converting Skript ...\n")

# get all the directory names and write them into a list of strings
dirs = os.listdir("./")

for dir in dirs:
    print ("Switching to directory: " + dir)
    os.chdir( "./".__add__(dir) )

    # Write all files in the dir in a list
    files = os.listdir(".")
    for file in files:
        # Convert the mp4 file into a mp3 file and delete the old mp4
        mp4_file = VideoFileClip(file)
        mp4_file.audio.write_audiofile(file[0:(len(file)-4)] + ".mp3") 
        os.remove(file)
    
    # Switch back to the main dir
    os.chdir("./..")      


##########################################################################################


print ("Starting Metadata Skript ...\n")

# iterate through all dirs and set the album name of every file to the name of the dir
for dir in dirs:
    print ("Switching to directory: " + dir)
    os.chdir( "./".__add__(dir) )

    files = os.listdir(".")
    for file in files:
        # Set Album Name and Artist
        audiofile = eyed3.load("./".__add__(file))
        audiofile.tag.album = dir
        audiofile.tag._getAlbumArtist = "Various Artists"

        if (audiofile.tag == None):
            audiofile.initTag()

        audiofile.tag.save()

    # Switch back to the main dir
    os.chdir("./..")    

print("\nFinished setting the Album Metadata!")
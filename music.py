from pydoc import TextRepr
from re import A
from typing import final
from moviepy.editor import TextClip
from moviepy.editor import*
import numpy as np
import imageio_ffmpeg
import os
from moviepy.config import check
os.environ["IMAGEMAGICK_BINARY"] = r"C:\Program Files\ImageMagick-7.1.0-Q16-HDRI\convert.exe"


# Import the video file
video = VideoFileClip("videoplayback.mp4")

# Set the start and end time for the clip (in seconds)
start_time = [00,245,465,662,941,1211,1544,1839,2195,2505,2746,2947,3191,3385,3615,3893,4153,4351,4531,5040,5274,5481,5736,5946,6444,6616,6871,7081,7367,7611,7847,8027,8255,8695]  
end_time =  [245,465,662,941,1211,1544,1839,2195,2505,2746,2947,3191,3385,3615,3893,4153,4351,4531,5040,5274,5481,5736,5946,6444,6616,6871,7081,7367,7611,7847,8027,8255,8695,8966]
nom = ["Aruarian Dance","Another Reflection","Battlecry","Luv(sic)","Luv(sic) part2","Luv(sic) part3","Luv(sic) part4","Luv(sic) part5",
"Luv(sic) Grand Finale","Perfect Circle","Blessing It (remix)","Horn in the middle","Lady Brown","Kumomi","Highs 2 Lows","Beat laments the world","Letter from Yokosuka","Think Different","A day by atmosphere supreme",
"Next view","Latitude (remix)","F.I.L.O.","Summer Gypsy","The Final View","Peaceland","Feather","reflection eternal","Eclipse","The Sign","Thank you","flowers",
"sea of cloud","Light on the land","Horizon","Winter Lane"]
numero = ["1","3","13","6","21","9","16","11","2","4","18","15", "7","10","27","26","14","28","12","25","17","20","8","22","19 ","23","24","5"]


for i in range(28):

    # Create the clip
    clip = video.subclip(start_time[i], end_time[i])

    # Export the clip to an mp3 file
    clip.audio.write_audiofile(numero[i]+"."+nom[i]+".mp3")

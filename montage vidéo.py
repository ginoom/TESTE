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

    #liste de music
music =["1.Ambulo x mell-ø - Luminescence ",
"2.BluntOne - Reflections",
"3.Jordy Chandra - Late Night Call",
"4.Kupla - Owls of the Night",
"5.Mondo Loops - Lunar Drive",
"6.YS - Snowman",
"7.Pandrezz - Cuddlin",
"8.Purrple Cat - Alone Time",
"9.j'san x epektase - snow & sand",
"10.mell-ø - Nova",
"11.rook1e x tender spring - the places we used to walk",
"12.imagiro - wool gloves",
"13.Aso - espresso",
"14.dryhope - Steps",
"15.G Mills - Keyframe",
"16.DLJ x BIDØ - Explorers",
"17.cocabona x Glimlip - Drops",
"18.Fatb - Cotton Cloud",
"19.ENRA - amber",
"20.goosetaf x the fields tape x francis - carried away",
"21.Glimlip x Yasper - I'm sorry",
"22.HM Surf - Single Phial",
"23.mvdb - breeze",
"24.less.people - Gyoza",
"25.Psalm Trees - fever",
"26.H.1 - Circle",
"27.Sarcastic Sounds - Wish You Were Mine"]
for i in range(27):

    #importer la music 
    audioclip = AudioFileClip("Oranji Projet/Playlist N°8/Music/" + music[i] + ".mp3")
    time = audioclip.duration

    #importer le fond
    videoclip = VideoFileClip("Oranji Projet/Playlist N°8/Fond de vidéo/fond.mp4")
    videoclip = videoclip.subclip(0,time)
    
    
    txt_clip = TextClip(music[i],fontsize = 10 ,  font='ARCADE_I.TTF', color='darkorange')
    txt_clip = txt_clip.set_position(('left', 'top')).set_duration(time)
    #création de la vidéo  

 
    video_with_new_audio = videoclip.set_audio(audioclip)

    final_video = CompositeVideoClip([video_with_new_audio,txt_clip])

    final_video.write_videofile(music[i]+".mp4")

    print ( music[i] + " fini" ) 




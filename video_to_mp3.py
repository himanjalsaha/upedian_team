import sys
from moviepy.editor import *
a=input("location of the video: ")
mp4_file = (a+'.mp4')
SAVE_PATH = input("where do you want to save the audio file: ")
c=(SAVE_PATH+"\\")
if SAVE_PATH=="Downloads" or SAVE_PATH=="downloads":
    c="C:\\Users\\mehul\\Downloads\\"
if SAVE_PATH=="Music" or SAVE_PATH=="music":
    c="D:\\music\\"
if SAVE_PATH=="ytdownloader" or SAVE_PATH=="yt":
    c="D:\\ytdownloader\\"
b=input("what do you want the name of the audio file to be: ")
mp3_file = (c+b+".mp3")
videoclip = VideoFileClip(mp4_file)
audioclip = videoclip.audio
audioclip.write_audiofile(mp3_file)
audioclip.close()
videoclip.close()
input("Hit enter to exit!")
sys.exit()
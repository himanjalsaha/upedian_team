import win32clipboard
import asset
import cipher
from pytube import YouTube
import sys
d='yes'
while d=='yes' or d=='y':
    link = input("enter the link of the video: ")
    try:
        # get clipboard data
        win32clipboard.OpenClipboard()
        link = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
    except Exception as ex:
        print('Error : ',ex)
        exit()
    try:
        #where to save 
        SAVE_PATH = "D:\\ytdownloader"
        yt = YouTube(link)
        print('Title :',yt.title)
        print('Available formats :')
        for stream in yt.streams.all():
            print(stream)
        itag = input('\nP.S. choose the ones with prograssive="True" for audio and video combined\nEnter the itag number to download video of that format: ')
        stream = yt.streams.get_by_itag(itag)
        print('\nDownloading--- '+yt.title+' into location : '+SAVE_PATH)
        stream.download(SAVE_PATH)
        input('Hit Enter to exit')
        d=input("do you want to try again?: ")
    except Exception as e: 
        print("Error",e) #to handle exception
        d=input("do you want to try again?: ")
if d=='no' or d=='n':
    print("exit!!!")
    sys.exit()

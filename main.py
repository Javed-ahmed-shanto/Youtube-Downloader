from pytube import YouTube
from sys import argv

link = argv[1] # give your link in the terminal after your file name within a quote
yt = YouTube(link)

print("Title: ", yt.title)

print("view: ", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download("C:/Users/Shanto/Downloads/Video")
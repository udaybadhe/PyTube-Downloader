#import os
#from moviepy.editor import *
from pytube import Search
from pytube import YouTube
def query_pars(a):
	s = Search(a)
	yt = YouTube(s.results[0].watch_url)
	r = yt.streams.filter(only_audio=True)
	s = yt.streams.get_by_itag(140)
	s.download('D://uni')
a = input("Enter the Song name: ")
query_pars(a)

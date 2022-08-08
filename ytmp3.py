from pytube import Search
import os
def query_pars(a):
	s = Search(a)
	link = s.results[0].watch_url
	os.system('youtube-dl.exe -x --audio-format mp3 {}'.format(link))
a = input("Enter the Song name: ")
query_pars(a)

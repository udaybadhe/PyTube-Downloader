from pytube import Search
import os
def query_pars(song_name):
	s = Search(song_name)
	link = s.results[0].watch_url
	os.system('yt-dlp.exe -x --audio-format mp3 {}'.format(link))
input_query = input("Enter the Song name: ")
query_pars(input_query)


import html5lib
from urllib.request import urlopen
import json
import sys
import datetime


if(sys.argv[1]=='e' or sys.argv[1]=='E'):
	# Corresponding json api url for eclectic24 
	url = "https://tracklist-api.kcrw.com/Music"
	song_list='Eclectic24_song_list.txt'
elif(sys.argv[1]=='n' or sys.argv[1]=='N'):
	# Corresponding json api url for KCRW's normal radio station
	url = "http://tracklist-api.kcrw.com/Simulcast"
	song_list='Normal_KCRW_Radio_song_list.txt'

# if(sys.argv[2] != None):
# 	url= url + '/' + string(sys.argv[2]) + '?time=' + sys.argv[3]


#get json data as a string from the kcrw api which is  url
page_info = str(urlopen(url).read(),'utf-8')

#load json object form the string
track=json.loads(page_info)


#open or create csv file to store song onto if it exists or not and insert song
with open(song_list,'a') as f:
	f.write(track['title'] + '---' + track['artist'] + '---' + track['album'] + "\n")




""" be carefule of "Breaks" 
Things to do:
Implement date searching by going through JSON list and using datetime objects for comparison
store in a txt file

"""

set_times=[]








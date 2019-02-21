from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel 
from youtube_dl import YoutubeDL

#part1:
url = "https://www.apple.com/itunes/charts/songs"
data = urlopen(url)

my_object = data.read()
shown = my_object.decode("utf8")

soup = BeautifulSoup (shown, "html.parser")
section = soup.find('section', 'section chart-grid')
div = section.find("div")
ul = div.find('ul')
li_list = ul.find_all("li")

list_of_songs = []
for li in li_list:
    name_song = li.h3.a.text
    artist = li.h4.a.text
    pair = {
        "name of song": name_song,
        "artist": artist,
    }
    list_of_songs.append(pair)

#pyexcel.save_as(records = list_of_songs, dest_file_name = "Artist and their song.xlsx" )


#part2:
options = {
    "default_search": "ytsearch",
    "max_downloads": 1,
}
for vid in list_of_songs:
    d = YoutubeDL(options)
    d.download([vid["name of song"] + vid["artist"]])

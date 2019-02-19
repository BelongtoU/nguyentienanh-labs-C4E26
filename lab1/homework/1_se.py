from urllib.request import urlopen
from bs4 import BeautifulSoup


url = "https://www.apple.com/itunes/charts/songs"
data = urlopen(url)
my_object = data.read()
shown = my_object.decode("utf8")

# with open("topsong.html", "wb") as k:
#     k.write(shown)


soup = BeautifulSoup (shown, "html.parser")
section = soup.find('section', 'section chart-grid')
print(section.prettify())

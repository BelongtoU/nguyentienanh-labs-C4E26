from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://aqicn.org/city/beijing/"
page = urlopen(url)
raw_data = page.read()
data = raw_data.decode('utf8', "replace")
soup = BeautifulSoup(raw_data, "html.parser")
div = soup.find("div", id = "citydivmain")
table = div.find("table", "api")
td = table.find_all("td")
print(td)

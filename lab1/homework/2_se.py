from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"

o_data = urlopen(url)
r_data = o_data.read()
decoded_data = r_data.decode("utf8")
soup = BeautifulSoup(decoded_data, "html.parser")

table = soup.find("table", id = "tblGridData")
td = table.find_all("td", "h_t")

keys_of_dict = []
for i in td:
    x = i.get_text()[22:]
    keys_of_dict.append(x)
keys_of_dict.insert(0, " ")

table1 = soup.find("table", id="tableContent")
result = []
id_list = ['01', '02', '10', '10', '11', '20', '21', '22', '23', '24', '25', '26', '30', '31', '32', '40', '50', '51', '52', '60', '61', '62', '70', '80', '81']

for i in id_list:
    tr = table1.find("tr", id = i)
    td_list = tr.find_all("td")
    line1 = []
    for x in td_list:
        t = x.get_text()
        line1.append(t)
    result.append(line1)


lines = []
for i in range(len(result)):
    new_line = {
        keys_of_dict[0]: result[i][0],
        keys_of_dict[1]: result[i][1],
        keys_of_dict[2]: result[i][2],
        keys_of_dict[3]: result[i][3],
        keys_of_dict[4]: result[i][4],
    }
    lines.append(new_line)
pyexcel.save_as(records = lines, dest_file_name = "table.xlsx")
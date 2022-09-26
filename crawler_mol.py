# 勞動部
# 撈新聞稿
# 列出新聞稿標題及更新日期
import requests
from bs4 import BeautifulSoup

url = "https://www.mol.gov.tw/1607/1632/1633/"
res = requests.get(url)
# print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
ret = soup.find_all("div", {"class":"item_list2"})
# print(ret)
# print(ret.text)
for s in ret:
  print(s.find("a").text)
  print(s.find_all("span")[1].text)
  print("============================")
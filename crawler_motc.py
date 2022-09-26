# 交通部 - 最新新聞
import requests
from bs4 import BeautifulSoup

url = "https://www.motc.gov.tw/ch/index.jsp"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
ret = soup.find("div", {"id":"accesskey"}).find_all("span", {"class": "left"})
for s in ret:
  # print(s)
  print(s.text)

# 建議抓 id
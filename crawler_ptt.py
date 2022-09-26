'''
爬取 PTT 八卦版文章標題

使用 Python 的 Requests 和 Beautiful Soup 函式庫，實作一個網路爬蟲
，利用傳送 cookie 的方式，突破未滿十八歲的按鈕檢查限制，取得 PTT 八卦版文章的標題
'''
# # 引入套件
# import requests

# # 使用 get 方法
# # web = requests.get('https://www.ptt.cc/bbs/Gossiping/index.html')
# # 加入 Cookies 資訊
# web = requests.get('https://www.ptt.cc/bbs/Gossiping/index.html', cookies={'over18':'1'})  
# # 讀取並印出 text 屬性
# print(web.text)


import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/'
web = requests.get('https://www.ptt.cc/bbs/Gossiping/index.html', cookies={'over18':'1'})
soup = BeautifulSoup(web.text, "html.parser")
# 取得 class 為 title 的 div 內容
titles = soup.find_all('div', class_='title')     
for i in titles:
    # 判斷如果不為 None
    if i.find('a') != None:           
        # 取得 div 裡 a 的內容，使用 get_text() 取得文字              
        print(i.find('a').get_text())              
        # 使用 ['href'] 取得 href 的屬性   
        print(url + i.find('a')['href'], end='\n\n')  





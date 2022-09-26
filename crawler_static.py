# 引入套件
import requests

'''
爬取 台灣水庫即時水情
https://water.taiwanstat.com/
'''
# # 使用 get 方法
# web = requests.get('https://water.taiwanstat.com/')  
# # 讀取並印出 text 屬性
# print(web.text)    


'''
讀取一個不存在的網頁，接著判斷如果 status_code 為 404，印出「找不到網頁」的文字
'''
web = requests.get('https://data.kcg.gov.tw/12345')
if web.status_code == 404:
    print('找不到網頁')

'''
使用 get 的方式發送 request 給範例的網址，並會加入 params 參數，當網址收到資料後，就會回傳指定的文字
'''
# # 設定參數
# params = {
#     'name':'kedugaw',
#     'age':'18'
# }
# # 加入參數
# web = requests.get('https://script.google.com/macros/s/AKfycbw5PnzwybI_VoZaHz65TpA5DYuLkxIF-HUGjJ6jRTOje0E6bVo/exec', params=params)
# print(web.text)
'''
爬取臺灣銀行牌告匯率
爬取牌告匯率 CSV
'''
# 引用套件
import requests

# 牌告匯率 CSV 網址
url = 'https://rate.bot.com.tw/xrt/flcsv/0/day'   
# 爬取網址內容
rate = requests.get(url)   
# 調整回應訊息編碼為 utf-8，避免編碼不同造成亂碼
rate.encoding = 'utf-8'   
# 以文字模式讀取內容 
rt = rate.text             
# 使用「換行」將內容拆分成串列
rts = rt.split('\n')       

# 讀取串列的每個項目
for i in rts:      
    # 使用 try 避開最後一行的空白行        
    try:     
        # 每個項目用逗號拆分成子串列                        
        a = i.split(',')             
        # 取出第一個 ( 0 ) 和第十三個項目 ( 12 )
        print(a[0] + ': ' + a[12])   
    except:
        break
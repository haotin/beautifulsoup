from bs4 import BeautifulSoup
import requests
import time
url='http://data.10jqka.com.cn/market/yybhyd/#refCountId=data_55a3b8e9_57'


def get_info(url,data = None):
    time.sleep(2)
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    names = soup.select('#J-ajax-main > table > tbody > tr > td > a')
    buys = soup.select('#J-ajax-main > table > tbody > tr > td.c-rise')
    sells = soup.select('#J-ajax-main > table > tbody > tr > td.c-rise')
    stocks =soup.select('#J-ajax-main > table > tbody > tr > td > div')
    if data == None:
        for name,buy,sell,stock in zip(names,buys,sells,stocks):
            data={
                'name':name.get_text(),
                'buy' :buy.get_text(),
                'sell':sell.get_text(),
                'stock':stock.get_text()
            }
            print (data)
get_info(url)


'''
使用headers 模拟浏览器
headers＝｛'User-Agent':'',
'Cookie':''
｝
'''
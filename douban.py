from bs4 import BeautifulSoup
import requests
'''
包含网页顺序变化的链接在列表解析式方式下改变
包含headers 模拟用户cooks登陆
'''
url = 'https://movie.douban.com/top250?start=0&filter='
#列表解析式构建列表集合
urls = ['https://movie.douban.com/top250?start={}&filter='.format((str(i))) for i in range(0,250,25)]

#使用headers 模拟浏览器
headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',
'Cookie':'bid="WLs6PI9gT1E"; gr_user_id=730a8d92-b176-45a6-ba88-b11580d021c9; viewed="3288908_10590856"; ll="118221"; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1471361754%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D_Hqyiq5TNRDVdQ1lMUIXJ0iXd8gLMxCajD7ql_hAku_XN-JZN5AU74fQX5j005ErAGjcWbovOOcEFXoz-OUFHH4_QjStVbMaby2I4z_C_Ie%26wd%3D%26eqid%3Dcf3c4c9a0018b19d0000000256dbc917%22%5D; ck=zXYc; ps=y; __utmt_douban=1; as="https://movie.douban.com/top250?start=0&filter="; dbcl2="149870921:dFIJ7lwyBKE"; push_noty_num=0; push_doumail_num=0; _pk_id.100001.4cf6=1488f81a4175b6a5.1457244474.3.1471363471.1471263816.; _pk_ses.100001.4cf6=*; __utma=30149280.1884180237.1451310274.1464102645.1471361754.7; __utmb=30149280.9.10.1471361754; __utmc=30149280; __utmz=30149280.1464102645.6.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.1968551725.1457244474.1457244474.1471361754.2; __utmb=223695111.0.10.1471361754; __utmc=223695111; __utmz=223695111.1457244474.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ap=1'
          }
info=[]

def get_info(url):
    wb_data=requests.get(url,headers=headers)

    soup=BeautifulSoup(wb_data.text,'lxml')
    titles = soup.select('#content > div > div.article > ol > li > div > div.info > div.hd > a > span')
    rates = soup.select('#content > div > div.article > ol > li > div > div.info > div.bd > div > span.rating_num')

    for title,rate in zip(titles,rates):
        data = {
            'title':title.get_text(),
            'rate':rate.get_text()

        }
        info.append(data)
        for i in info:
            if float(i['rate'])>9.3:
                #print (i['title'],i['rate'])
                print (info)
for i in urls:
    get_info(i)


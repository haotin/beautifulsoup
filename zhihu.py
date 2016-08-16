from bs4 import BeautifulSoup
import requests

url='https://www.zhihu.com/people/dong-xin-zhu/answers'



wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')
questions = soup.select('#mi-1471058839 > h2 > a')
answers = soup.select('#mi-1471058839 > div > div.zm-item-rich-text.expandable.js-collapse-body > div')

print (soup)
'''
for question,answer in zip(questions,answers):
    data={
        'question':question.get_text(),
        'answer' :answer.get_text()
    }
    print (data)
'''
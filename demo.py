from bs4 import BeautifulSoup
import requests

url='https://www.zhihu.com/people/ji-xuan-yi-9'



wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')
questions = soup.select('#zh-profile-activity-page-list > div:nth-child > div.zm-profile-section-main.zm-profile-section-activity-main.zm-profile-activity-page-item-main > a.question_link')
answers = soup.select('#zh-profile-activity-page-list > div.zm-profile-section-item.zm-item.clearfix.zm-item-expanded > div.zm-item-answer > div.zm-item-rich-text.expandable.js-collapse-body > div')


for question,answer in zip(questions,answers):
    data={
        'question':question.get_text(),
        'answer' :answer.get_text()
    }
    print (data)

import requests
from bs4 import BeautifulSoup 
import pandas as pd
import schedule
import time
import telepot

#### 데이터 수집 함수 ####

def collect_data(url):
    # 1. Send an HTTP request to the website and retrieve the HTML content
    response = requests.get(url)

    # 2. Use BeautifulSoup to parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    # print(soup)

    # 3. Extract the data you are interested in
    # 종가 가져오기
    last_price = soup.find("span", {"class": "value"}).text.strip()

    print(last_price)

    # table = soup.find_all('div', class_ = 'box_type_m') # 지수 모음집
    # # print(table)
    # rows = table[0].find_all('tr')
    # data = []
    # for row in rows:
    #     cols = row.find_all('td', class_ = 'number_1')
    #     cols = [col.text for col in cols]
    #     data.append(cols)

    # # Use pandas to store and manipulate the data
    # df = pd.DataFrame(data)
    # print(df)

'''
schedule.every().day.at("08:00").do(collect_data)

while True:
    schedule.run_pending()
    time.sleep(1)

#### 엑셀 시트 생성 함수 ####

#### TelegramChatBot ####

# Sending the data on Telegram
    bot = telepot.Bot(token='60950303AAGG_IqTO109_rAMP56OMh0_f7P5aOo3G2U43:')
    chat_id = '1135987650'
    bot.sendMessage(chat_id, text=df)

token = '60950303AAGG_IqTO109_rAMP56OMh0_f7P5aOo3G2U43:' # Telebot에게 받은 봇 API 토큰
mychid = '1135987650' # userinfobot에서 받은 값
bot = telepot.Bot(token)
 
 
def handle(message):
    print(message)
    bot.sendMessage(mychid, '멍충이')
 
 
MessageLoop(bot, handle).run_as_thread()
 
while True:
    pass

'''
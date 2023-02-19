import requests
from bs4 import BeautifulSoup
import pandas as pd
import schedule
import time
import telepot

def collect_data():
    # Send an HTTP request to the website and retrieve the HTML content
    url = 'https://www.federalreserve.gov/releases/h3/current/default.htm'
    response = requests.get(url)
    html_content = response.content

    # Use BeautifulSoup to parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract the data you are interested in
    table = soup.find('table', {'class': 'data'})
    rows = table.find_all('tr')
    data = []
    for row in rows:
        cols = row.find_all('td')
        cols = [col.text for col in cols]
        data.append(cols)

    # Use pandas to store and manipulate the data
    df = pd.DataFrame(data)
    print(df)
    # Sending the data on Telegram
    bot = telepot.Bot(token='60950303AAGG_IqTO109_rAMP56OMh0_f7P5aOo3G2U43:')
    chat_id = '1135987650'
    bot.sendMessage(chat_id, text=df)

schedule.every().day.at("10:00").do(collect_data)

while True:
    schedule.run_pending()
    time.sleep(1)
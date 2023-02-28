from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import sqlite3
from bs4 import BeautifulSoup

# investing.com에서 데이터를 가져와서 데이터베이스에 저장하는 함수
def get_macro_data():
    url = 'https://kr.investing.com/portfolio/?portfolioID=NzE3bW4xYjY0Z29mMGEzMA%3D%3D'

    # 로그인 정보
    email = 'YOUR_EMAIL'
    password = 'YOUR_PASSWORD'

    # Chrome driver options 설정
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-gpu')

    # Chrome driver 실행
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    # 로그인
    email_input = driver.find_element_by_name('email')
    password_input = driver.find_element_by_name('password')
    email_input.send_keys(email)
    password_input.send_keys(password)
    password_input.send_keys(Keys.ENTER)

    # 데이터 수집
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'bold')))
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    conn = sqlite3.connect('macro_data.db')
    cursor = conn.cursor()

    for row in soup.find_all('tr', {'class': 'bold'}):
        date = row.find('td', {'class': 'first left'}).text.strip()
        index_name = row.find('td', {'class': 'left name'}).text.strip()
        value = row.find('td', {'class': 'last right'}).text.strip()

        cursor.execute('''
            INSERT INTO macro_data (date, index_name, value) VALUES (?, ?, ?)
        ''', (date, index_name, value))

    conn.commit()
    conn.close()

    # Chrome driver 종료
    driver.quit()

get_macro_data()
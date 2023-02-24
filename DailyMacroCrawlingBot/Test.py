from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

options = Options()
options.headless = True
service = Service('/Users/won-yooseung/Desktop/14_CrawlingBot/chromedriver_mac_arm64/chromedriver') # Chrome 드라이버 경로
driver = webdriver.Chrome(service=service, options=options)

url = "https://kr.investing.com/portfolio/?portfolioID=NzE3bW4xYjY0Z29mMGEzMA%3D%3D"
driver.get(url)

# 종가 가져오기
price_element = WebDriverWait(driver, 20).until(
    presence_of_element_located((By.ID, '39985521_last_942611')))
price = price_element.text

print("종가:", price)

driver.quit()
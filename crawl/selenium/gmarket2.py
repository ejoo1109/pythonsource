from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# wait 을 위한 모듈
from selenium.webdriver.support.ui import WebDriverWait

# 마우스나 키보드를 조작하는 모듈
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 파싱을 위한 모듈
from bs4 import BeautifulSoup

import time

# webdriver설정
driver = webdriver.Chrome("./driver/chromedriver")
driver.implicitly_wait(3)
# 특정 사이트 지정
driver.get("http://gtour.gmarket.co.kr/TourV2/Item?GoodsCode=1672783002")

print(driver.page_source)

WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "h1.itemtit"))
)

soup = BeautifulSoup(driver.page_source, "html.parser")

print(soup.select_one("h1.itemtit").text)

time.sleep(3)

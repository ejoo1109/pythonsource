# youtube에서 원하는 가수 검색어 넣고 목록 중에서 title만 추출하기
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("./driver/chromedriver")

driver.get("http://youtube.co.kr")

element = driver.find_element_by_name("search_query")
element.send_keys("아이유")
element.send_keys(Keys.ENTER)

# time.sleep(3)
driver.implicitly_wait(3)

titles = driver.find_elements_by_tag_name("h3")

for title in titles:
    print(title.text)
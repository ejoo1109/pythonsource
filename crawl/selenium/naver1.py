# 네이버에 원하는 검색어 넣고 결과 페이지 띄우기
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # Keys.ENTER 사용하려면 import추가
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("./driver/chromedriver")

driver.get("http://naver.com")

# element = driver.find_element_by_name("query")
element = driver.find_element(By.NAME, "query")
element.send_keys("갤럭시")
element.send_keys(Keys.ENTER)
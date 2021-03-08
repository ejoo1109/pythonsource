from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # Keys.ENTER 사용하려면 import추가
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("./driver/chromedriver")

driver.get("http://gmarket.co.kr")

# element = driver.find_element_by_name("keyword")
element = driver.find_element(By.NAME, "keyword")
element.send_keys("운동화")
element.send_keys(Keys.ENTER)
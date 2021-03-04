# selenium
# 목적 : 웹을 테스트하는 프레임 워크
# 브라우저 자동화 => 브라우저를 조작하여 일을 시킬 수 있음
# 각 브라우저마다 웹 드라이버를 통해서 자동화 시킴
from selenium import webdriver
import time

driver = webdriver.Chrome("./driver/chromedriver")
driver.implicitly_wait(3)  # time.sleep(3)와 같은 개념 드라이버가 로드되는데 걸리는 시간

# 브라우저 크기 조정
driver.maximize_window()  # 최대크기

driver.get("http://www.naver.com")



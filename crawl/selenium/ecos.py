# https://ecos.bok.or.kr/EIndex.jsp 100대 지표 클릭후 한눈에 보는 통계지표 엑셀 다운로드

from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # Keys.ENTER 사용하려면 import추가
import time

# webdriver설정
driver = webdriver.Chrome("./driver/chromedriver")

# 특정 사이트 지정
driver.get("https://ecos.bok.or.kr/EIndex.jsp")

# 100대 통계지표 클릭
driver.find_element_by_css_selector(".ESsubject > ul > li:nth-child(1) > a").click()

# 새창으로 제어권 넘기기
driver.switch_to.window(driver.window_handles[1])
driver.implicitly_wait(2)  # 제어권을 넘기고 태그가 넘어 올때까지 시간을 줘야함

# 엑셀 다운로드 클릭
driver.find_element_by_css_selector(".HScontent-header fieldset a").click()

time.sleep(2)
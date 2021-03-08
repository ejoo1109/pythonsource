# daum 접속 후 원하는 기사 클릭 후 이동
# 기사 상세보기에서 기사제목 출력하기

from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # Keys.ENTER 사용하려면 import추가
import time

# webdriver설정
driver = webdriver.Chrome("./driver/chromedriver")

# 특정 사이트 지정
driver.get("https://daum.net")

# 기사 클릭
driver.find_element_by_css_selector(".list_thumb > li:nth-child(2)").click()

# 기사제목 출력
print(driver.find_element_by_tag_name("h3").text)

time.sleep(5)
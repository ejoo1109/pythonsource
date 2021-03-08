from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # Keys.ENTER 사용하려면 import추가
import time

# webdriver설정
driver = webdriver.Chrome("./driver/chromedriver")

# 특정 사이트 지정
driver.get("http://daum.net")

# 세션 아이디, 쿠키값 출력
print("Session ID : {}".format(driver.session_id))
print("Cookies : {}".format(driver.get_cookies))

# 검색어 넣고 엔터치기
# find_element와 find_elements 구별 주의 find_element는 리스트로 반환
element = driver.find_element_by_name("q")
element.send_keys("아이폰")
element.send_keys(Keys.ENTER)

# 브라우저 뒤로가기 클릭
driver.back()  # 앞으로 가기 - driver.forward() : 앞으로 가기

time.sleep(3)

# 다나와 사이트 접속 후 로그인 클릭, 아이디, 비밀번호 입력후 로그인 자동화
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # Keys.ENTER 사용하려면 import추가
import time

# webdriver설정
driver = webdriver.Chrome("./driver/chromedriver")

# 특정 사이트 지정
driver.get("http://danawa.com")

# 로그인 클릭
driver.find_element_by_css_selector(".my_page_service").click()

# 아이디 입력
userid = driver.find_element_by_id("danawa-member-login-input-id")
userid.clear()  # 기존아이디가 남아있는경우 삭제
userid.send_keys("")

# 비밀번호 입력
userpw = driver.find_element_by_id("danawa-member-login-input-pwd")
userpw.clear()  # 기존비밀번호가 남아있는경우 삭제
userpw.send_keys("")
userpw.send_keys(Keys.ENTER)
# driver.find_element_by_id("danawa-member-login-loginButton").click()

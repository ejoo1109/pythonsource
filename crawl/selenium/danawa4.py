# 다나와 자동로그인 + 제품 검색 + 첫번째제품명 클릭
# + 관심상품 담기 + 관심상품 리스트 출력하기
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# wait 을 위한 모듈
from selenium.webdriver.support.ui import WebDriverWait

# 마우스나 키보드를 조작하는 모듈
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

# 파싱을 위한 모듈
from bs4 import BeautifulSoup

# 엑셀 저장
import openpyxl

# 이미지 요청
import requests

# 가짜 브라우저
from fake_useragent import UserAgent

# 이미지 바이트 처리
from io import BytesIO

import time

# 엑셀 저장과 관련된 코드
workbook = openpyxl.Workbook()
# 기본 워크시트 활성화
worksheet = workbook.active

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

# 검색어 넣기
search = driver.find_element_by_id("AKCSearch")
search.clear()
search.send_keys("세탁기")
search.send_keys(Keys.RETURN)
time.sleep(3)

# 제조사 클릭
driver.find_element_by_xpath(
    "//*[@id='SearchOption_Maker_Rep']/div[1]/div/label/span[1]"
).click()

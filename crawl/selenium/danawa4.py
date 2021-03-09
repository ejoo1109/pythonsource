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

# webdriver설정
driver = webdriver.Chrome("./driver/chromedriver")

# 특정 사이트 지정
driver.get("http://danawa.com")

# 로그인 클릭
login = driver.find_element_by_css_selector(".my_page_service").click()

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
search.send_keys(Keys.ENTER)

# 검색결과가 나올 때까지 기다리기
time.sleep(5)

# 제조사 클릭
driver.find_element_by_xpath(
    "//*[@id='SearchOption_Maker_Rep']/div[1]/div/label/span[1]"
).click()

# 품목 클릭
driver.find_element_by_xpath(
    "//*[@id='newSearchOptionArea']/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div/label/span[2]"
).click()

# 세탁기 용량 더보기 클릭 후 기다리기
WebDriverWait(driver, 3).until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            "//*[@id='newSearchOptionArea']/div[2]/div[2]/div[4]/div[1]/div[2]/div[2]/button[1]",
        )
    )
).click()

# 18kg 클릭
WebDriverWait(driver, 3).until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            "//*[@id='SearchOption_RepOption_92_All']/div/div[9]/div/label/span",
        )
    )
).click()

# 클릭한 옵션에 따라 상품 내용이 페이지에 보여주기 위한 시간
time.sleep(3)

# 보여지는 상품 목록 중 첫번째 상품 클릭
driver.find_element_by_css_selector(
    "#productItem12964949 > div > div.prod_info > p > a"
).click()

# 새창으로 제어권 넘기기
driver.switch_to.window(driver.window_handles[1])

# 관심상품 클릭
driver.find_element_by_css_selector("#interest > span.ico_interest").click()

# 관심상품 담기
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            "//*[@id='wishFolder_101516130']",
        )
    )
).click()

# 관심상품 리스트로 가기
driver.find_element_by_css_selector(
    "div.my_service_list3 > ul > li.interest_goods_service > a"
).click()

time.sleep(3)

# 상세 페이지
soup = BeautifulSoup(driver.page_source, "html.parser")


wishlist = soup.select("#wishProductListArea > table > tbody > tr")

for idx, item in enumerate(wishlist, 1):
    product_name = item.select_one("td.info > div.tit > a").text
    product_spec = item.select_one("td.info > dl.spec > dd > a").text
    product_price = item.select_one("td.lowest > dl > div.cost > span > em").text

    print("[{}] {}".format(idx, product_name))
    print("{}".format(product_spec))
    print("{}".format(product_price))
    print()

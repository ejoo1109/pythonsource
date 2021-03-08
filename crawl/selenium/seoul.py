# https://sll.seoul.go.kr 서울시평생학습포털
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # Keys.ENTER 사용하려면 import추가
import time

# webdriver설정
driver = webdriver.Chrome("./driver/chromedriver")

# 특정 사이트 지정
driver.get("https://sll.seoul.go.kr")

# close2_14324326
# 팝업창 닫기
driver.find_element_by_css_selector("#close2_14324326 > img").click()
# 통합검색 클릭
driver.find_element_by_css_selector(".a-search-box > span").click()
# 검색어 넣기 + 엔터
element = driver.find_element_by_id("query")
element.send_keys("영어")
element.send_keys(Keys.ENTER)

# 새 창으로 제어권 넘기기
driver.switch_to.window(driver.window_handles[1])  # 16진수로 된 키값

# 확인
print(driver.current_url)

# 더 많은 결과보기 클릭
driver.find_element_by_class_name("btn-more-result").click()

# 여러강좌 타이틀 출력
titles = driver.find_elements_by_css_selector(
    ".search-result-list > ul > li > div strong"
)

for title in titles:
    print(title.text)

time.sleep(5)
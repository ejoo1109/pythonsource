# 네이버에 검색어를 입력하고 이미지 카테고리를 클릭한 후 스크롤 내리기
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# wait 을 위한 모듈
from selenium.webdriver.support.ui import WebDriverWait

# 마우스나 키보드를 조작하는 모듈
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

import time
import urllib.request as request
import os

driver = webdriver.Chrome("./driver/chromedriver")
driver.implicitly_wait(3)

driver.get("https://www.naver.com")
driver.maximize_window()

# 검색어 입력하는 요소 찾기
element = driver.find_element_by_id("query")
# 검색어 입력
element.send_keys("강아지")
# 엔터
element.send_keys(Keys.ENTER)
# 전체 검색 결과 페이지에서 이미지 탭 클릭
driver.find_element_by_css_selector("ul.base > li:nth-child(2) > a").click()


# img 태그 가져오기
# main_pack > section > div._contentRoot.image_wrap > div.photo_group._listGrid > div.photo_tile._grid > div:nth-child(1) > div > div.thumb > a > img

# 이미지가 보여지는 영역의 태그 기다리기
# 조건주기 - EC.presence_of_element_located(()) 데이터가 튜플로 들어가야하기 때문에(())로 처리
img_tiles = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div.photo_tile._grid"))
)

# 스크롤 이동
time.sleep(4)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight/2-200)")

time.sleep(5)

images = driver.find_elements_by_css_selector("div.thumb a img")

save_path = "c:\\imagedown\\"

idx = 1
for img in images:
    print(img.get_attribute("src"))  # 속성값을 가져올경우 get_attribute 사용
    file_name = os.path.join(save_path, save_path + str(idx) + ".png")
    request.urlretrieve(img.get_attribute("src"), file_name)
    idx += 1

time.sleep(2)
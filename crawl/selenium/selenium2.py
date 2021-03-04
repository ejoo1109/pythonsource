from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 웹 드라이버 로드
driver = webdriver.Chrome("./driver/chromedriver")


# 특정 사이트 지정
driver.get("http://www.daum.net")

# 테스트코드 -title 한번 더 확인
assert "Daum" in driver.title

# 현재 접속한 사이트 소스 가져오기
#print(driver.page_source) #driver - 이미 파싱 기능을 가지고 있다.

# 원하는 요소 찾기 - WebElement로 리턴
search = driver.find_element(By.NAME, "q") #NAME 기준 찾기 By.ID -id기준 찾기
# 검색어 입력 자동화
search.send_keys("안드로이드")
# 엔터치기 자동화
search.send_keys(Keys.ENTER) #라이브러리 추가
print(search)

driver.implicitly_wait(3)
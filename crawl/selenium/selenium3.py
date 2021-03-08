from selenium import webdriver

# webdriver설정
driver = webdriver.Chrome("./driver/chromedriver")

# 특정 사이트 지정
driver.get("http://python.org")

# 타이틀 출력
print(driver.title)

# 테스트코드 -title 한번 더 확인- 타이틀이 없다면 다음 전체소스 가져오기 안됨
assert "Python" in driver.title

# 전체 소스 가져오기
print(driver.page_source)
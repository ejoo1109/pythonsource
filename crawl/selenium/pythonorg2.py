# python.org에서 python으로 검색하고 검색 결과에서 타이틀만 추출하기
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# webdriver설정
driver = webdriver.Chrome("./driver/chromedriver")

# 특정 사이트 지정
driver.get("http://python.org")

# 타이틀 출력
print(driver.title)

# 테스트코드 -title 한번 더 확인- 타이틀이 없다면 다음 전체소스 가져오기 안됨
assert "Python" in driver.title

# 전체 소스 가져오기
# print(driver.page_source)

# element = driver.find_element_by_name("q") #name으로 찾을때
# element = driver.find_element_by_id("id-search-field") #id 로 찾을때
# element = driver.find_element_by_class_name("search-field") #class로 찾을때
# element = driver.find_element_by_css_selector("#id-search-field")
# xpath : 마우스 우클릭 copy //*[@id="id-search-field"]

element = driver.find_element_by_xpath("//*[@id='id-search-field']")
element.send_keys("python")
element.send_keys(Keys.ENTER)

# 검색 결과에서 타이틀만 추출하여 보여주기
# titles = driver.find_elements_by_tag_name("h3")
titles = driver.find_elements(By.TAG_NAME, "h3")

for title in titles:
    print(title.text)
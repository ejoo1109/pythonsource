# 하나의 브라우저에 여러개의 창 띄우기
from selenium import webdriver

driver = webdriver.Chrome("./driver/chromedriver")

driver.get("https://www.google.com")

print("현재 창 : {}".format(driver.title))

# 현재 활성화된 창에 대한 정보 가져오기
parent_window = driver.current_window_handle

# 자바 스크립트로 새로운 창 열기-execute_script: 자바스크립트 사용한다는 코드
driver.execute_script("window.open('https://www.naver.com')")

# 현재 브라우저에 열린 모든 창의 정보 가져오기- 리스트로 반환
# ['CDwindow-68D979ADB48CE714A8E440CF584AB979' #'CDwindow-D454DA11B089C4F83C353B319F00B7B6']
# child_window info : ['CDwindow-68D979ADB48CE714A8E440CF584AB979', #'CDwindow-D454DA11B089C4
all_windows = driver.window_handles
print(all_windows)

# 자식 창에 대한 정보 가져오기
child_window = [window for window in all_windows if window != parent_window[0]]
print("child_window info : {}".format(child_window))

# 자식 창으로 제어권 이동
driver.switch_to.window(child_window)
print("현재 창 : {}".format(driver.title))

# 자식창 닫기
driver.close()

# 부모 창으로 제어권 이동
driver.switch_to.window(parent_window)
print("제어권 확인 : {}".format(driver.title))
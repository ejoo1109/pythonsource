import urllib.request as request

# 정보를 가져올 url
html_url = "http://google.com"
# 이미지 가져오기
img_url = "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTAxMThfMjcy%2FMDAxNjEwOTQ1MDIyOTc0.AI3mcqFv-tdZkdEkaH3aWuvKtJZgoL9Cem0izgsIYFIg.zQ-zQwfBEKFVLXapDE15juPi5o57NrEC9OL4rmWz9c8g.PNG.dlscksspwlq%2F%25B0%25F1%25B5%25E7%25B8%25AE%25C6%25AE%25B8%25AE%25B9%25F6013.png&type=sc960_832"

# 가져온 정보를 저장할 위치
save_url = "c:/google.html"
save_img = "c:/dog.png"


try:
    # urlretrieve - 요청하는 url의 정보를 로컬파일로 저장
    file1, header1 = request.urlretrieve(html_url, save_url)
    file2, header2 = request.urlretrieve(img_url, save_img)
except Exception as e:
    print(e)
else:
    print(header1)
    print(header2)
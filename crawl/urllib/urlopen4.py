# 데이터를 읽고 저장까지 하는 경우
import urllib.request as request
from urllib.error import HTTPError

# 다운로드 경로 및 파일명
path_list = ["c:/dog.jpg", "c:/naver.html"]

# 다운로드 받을 이미지 및 파일 지정
target_url = [
    "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTAxMThfMjcy%2FMDAxNjEwOTQ1MDIyOTc0.AI3mcqFv-tdZkdEkaH3aWuvKtJZgoL9Cem0izgsIYFIg.zQ-zQwfBEKFVLXapDE15juPi5o57NrEC9OL4rmWz9c8g.PNG.dlscksspwlq%2F%25B0%25F1%25B5%25E7%25B8%25AE%25C6%25AE%25B8%25AE%25B9%25F6013.png&type=sc960_832",
    "http://www.naver.com",
]


# enumerate -하나씩 꺼내오면서 번호를 붙일 수 있음
for i, url in enumerate(target_url):
    try:
        response = request.urlopen(url)

        contents = response.read()

        print("*" * 50)
        print()
        print("Header info {} - {}".format(i, response.info()))
        print("Http Status Code {}".format(response.getcode()))
        print()
        print("*" * 50)

        # 파일저장
        with open(path_list[i],'wb') as f:
            f.write(contents)

    except HTTPError as e:
        print(e)
    else:
        print("succeed")
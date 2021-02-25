import urllib.request as request
from urllib.parse import urlencode

# 행정안전부 rss 정보 가져오기

rss = "https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"

params = []

for num in [1001, 1012, 1013, 1014]:
    params.append(dict(ctxCd=num))  # dict() 구조로 만들어주는 함수

print(params)

for p in params:
    param = urlencode(p)

    url = rss + "?" + param

    # url 확인
    print("url {}".format(url))
    
    # 정보 요청
    data = request.urlopen(url).read().decode("utf-8")

    print("*" * 100)
    print(data)
    print()
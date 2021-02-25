# 영화진흥 위원회 api - 일별 박스 오피스 가져온 후 파일 저장
import urllib.request as request
from urllib.error import HTTPError

# 정보를 가져올 url
url = "http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml?key=f5eef3421c602c6cb7ea224104795888&targetDt=20210224"

try:
    #file1, header1 = request.urlretrieve(url, "c:/movie.txt")
    data = request.urlopen(url).read().decode("utf-8")
#except Exception as e:
except HTTPError as e:
    print(e)
else:
    print("성공")
    with open("c:/movie.txt",'w') as f:
        f.write(data)
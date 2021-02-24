import urllib.request as request

# 좋아하는 연예인 사진 가져오기
img_url = "https://search.pstatic.net/common/?src=http%3A%2F%2Fimgnews.naver.net%2Fimage%2F312%2F2017%2F03%2F30%2F2017033016382311565-540x728_99_20170330164002.jpg&type=a340"

# 가져온 정보를 저장할 위치
save_img = "c:/gongyoo.png"


try:
    # urlretrieve - 요청하는 url의 정보를 로컬파일로 저장
    file2, header2 = request.urlretrieve(img_url, save_img)
except Exception as e:
    print(e)
else:
    print(header2)
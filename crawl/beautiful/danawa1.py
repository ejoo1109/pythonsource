# 로그인 이후에 확인 할 수 있는 정보 크롤링
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

# 로그인시 보내는 formData
login_info = {
    "redirectUrl": "http://www.danawa.com/",
    "loginMemberType": "general",
    "id": "아이디",
    "isSaveId": "true",
    "password": "",
}

headers = {
    "user-agent": UserAgent().chrome,
    # F12->Network -> requestheders에 위치
    "Referer": "https://auth.danawa.com/login?url=http%3A%2F%2Fwww.danawa.com%2F",
}

with requests.Session() as s:  # 로그인 작업 (헤더스같이보내기)
    # Origin: https://auth.danawa.com/login
    res = s.post("https://auth.danawa.com/login", login_info, headers=headers)
    # print(res.text)

    # 로그인 후 주문/배송 조회 클릭하기(헤더스같이보내기)
    res = s.get("https://buyer.danawa.com/order/Order/orderList", headers=headers)
    # print(res.text)

    soup = BeautifulSoup(res.text, "html.parser")

    # 로그인 성공 체크
    # wrap_shop_danawa > div.my_wish_bg > div > div.left_menu_bar > div.side_nav > div.nav_top > p
    check_id = soup.find("p", class_="user")

    if check_id is None:  # id가 없다면
        raise Exception("로그인 실패. 로그인 값 확인")  # 강제 에러발생 시키기

        # 주문내역 확인하기
        # 출력문 형태
        # **** My Order Info ***
        # 입금대기 : 0
        # 결제완료 : 0
        # 배송중 : 0
        # 배송완료 : 0
        # 취소중/취소완료 : 0

    info_list = soup.select("div.sub_info > ul.info_list > li")
    # print(info_list)
    print("**** My Order Info ***")
    for item in info_list:
        proc, val = item.find("span").string, item.find("strong").string.strip()
        # proc: span 의 텍스트 val : 공백제거후 텍스트
        print("{} : {}".format(proc, val))

import requests

# with = Session을 자동으로 열고 닫아줌
with requests.Session() as s:
    # timeout=0.001 -특정시간안에 응답이 오지 않을경우 에러
    r = s.get("https://api.github.com/events", timeout=0.001)

    # 수신 상태 체크 함수(상태 체크 시 이상이 있으면 다음 문장을 처리 안함)
    r.raise_for_status()

    print(r.text)
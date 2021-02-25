from fake_useragent import UserAgent

# 브러우저 우회 접속시 사용 -> request 요청할때 header에 같이 보냄
# 객체 생성
userAgent = UserAgent()

print(userAgent.ie)
print(userAgent.msie)
print(userAgent.chrome)
print(userAgent.safari)
print(userAgent.opera)
print(userAgent.firefox)
print(userAgent.random)
import urllib.request as request

weather_url = "https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109"

# urlopen - 웹에서 가져온 정보를 메모리 위에 올려 작업하는 형태
data = request.urlopen(weather_url).read()

text = data.decode("utf-8")

print(text[:4000])
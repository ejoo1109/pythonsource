# 네이트 뉴스에서 최신 급상승 뉴스 - 시사 제목 출력하기
import requests
from bs4 import BeautifulSoup
import xlsx_write as excel

url = "https://news.nate.com/recent?mid=n0100"

res = requests.get(url)

soup = BeautifulSoup(res.text, "html.parser")

sisa_list = soup.select("#sisa1 > ol > li")  
#print(sisa_list)

news_list = list() #news_list=[] 비어있는 리스트 생성
for title in sisa_list:
    print("{}".format(title.find('a').string))
    news_list.append([title.find('a').string])

#print(news_list)
#엑셀 파일로 저장하기
excel.write_excel_template("0303sisa.xlsx","시사",news_list)


  
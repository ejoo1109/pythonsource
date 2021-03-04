import re

# .search() : 문자열 전체를 검색해서 정규식과 매칭되는 패턴을 찾아서 리턴
# match() : 문자열 처음부터 정규식과 매칭되는 패턴을 찾아서 리턴
# sub() : 패턴을 찾고 바꾸기
# findall() : 정규 표현식과 매칭되는 모든 문자열을 리스트로 리턴
# split() : 찾은 정규표현식 패턴 문자열을 기준으로 문자열 분리

pattern = re.compile("[a-z]+")  # match():  None
print("match(): ", pattern.match("Dave"))  # 처음부터 일지하지 않으면 None
print("search(): ", pattern.search("Dave"))  # 포함만 되어있기만 하면되면 search사용

print()
data = "DDA D1A DDA DA"
# re.sub(패턴, 바꿀문자열, 원본문자열) : replace 개념
print(re.sub("D.A", "Dave", data))  # Dave Dave Dave DA

print()
print(
    pattern.findall("Game of Life in Python")
)  # 소문자만 추출 ['ame', 'of', 'ife', 'in', 'ython']
pattern = re.compile("[A-Za-z]+")
print(
    pattern.findall("Game of Life in Python")
)  # 대소문자 포함하여 리턴 ['Game', 'of', 'Life', 'in', 'Python']

pattern = re.compile("[a-z]+")
findalled = pattern.findall("GAME")
if len(findalled) > 0:  # 데이터가 맞다면 1이 반환되니깐..
    print("정규표현식에 맞는 문자열 존재")
else:
    print("정규표현식에 맞는 문자열 존재하지 않음")

print()
pattern = re.compile(":")
print(pattern.split("java:python"))  # : 콜론 기준으로 문자열 나눔 ['java', 'python']

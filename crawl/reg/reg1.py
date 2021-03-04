# 정규 표현식
import re  # 정규식 표현을 위한 라이브러리

# 패턴 정의
print("*** . 의미 : 문자 한개를 의미 ***")
pattern = re.compile("D.A")  # D.A -D와 A는 문자열, . 모든문자열

# .search()함수 - 패턴이 맞는지 확인
result = pattern.search("DAA")
print(result)  # <re.Match object; span=(0, 3), match='DAA'>

result = pattern.search("D1A")
print(result)  # <re.Match object; span=(0, 3), match='D1A'>

result = pattern.search("D00A")
print(result)  # None : 못찾을때 None으로 반환, 00 문자 두개로 인식하여 에러

result = pattern.search("DA")
print(result)  # None : 가운데 글씨 인식 못함

result = pattern.search("d0A")
print(result)  # None : 대소문자 구별하기 때문에 소문자 인식못함

result = pattern.search("d0A D1A 0999")
print(result)  # <re.Match object; span=(4, 7), match='D1A'> 해당되는 위치 반환

print("\n*** ? 의미 : 최소 0~1 매칭을 의미***")
pattern = re.compile("D?A")

print(pattern.search("A"))  # <re.Match object; span=(0, 1), match='A'>
print(pattern.search("DA"))  # <re.Match object; span=(0, 2), match='DA'>
print(
    pattern.search("DDDDDDDDDDDDDDDDDA")
)  # <re.Match object; span=(16, 18), match='DA'>  D가 많을경우 끝에서부터 0~1번째 반환

print("\n*** * 의미 : 0~무한대 의미, 0번째부터 무한대***")
pattern = re.compile("D*A")

print(pattern.search("A"))  # <re.Match object; span=(0, 1), match='A'>
print(pattern.search("DA"))  # <re.Match object; span=(0, 2), match='DA'>
print(
    pattern.search("DDDDDDDDDDDDDDDDDA")
)  # <re.Match object; span=(0, 18), match='DDDDDDDDDDDDDDDDDA'>

print()
pattern = re.compile("AD*A")  # D는 안나와도됨

print(pattern.search("AA"))  # <re.Match object; span=(0, 2), match='AA'>
print(pattern.search("ADA"))  # <re.Match object; span=(0, 3), match='ADA'>
print(
    pattern.search("ADDDDDDDDDDDDDDDDDDDDDDA")
)  # <re.Match object; span=(0, 24), match='ADDDDDDDDDDDDDDDDDDDDDDA'>

print("\n*** + 의미 : 1~무한대 의미, 최소1번은 찾고 무한대***")
pattern = re.compile("D+A")

print(pattern.search("A"))  # None
print(pattern.search("DA"))  # <re.Match object; span=(0, 2), match='DA'>
print(
    pattern.search("DDDDDDDDDDDDDDDDDA")
)  # <re.Match object; span=(0, 18), match='DDDDDDDDDDDDDDDDDA'>
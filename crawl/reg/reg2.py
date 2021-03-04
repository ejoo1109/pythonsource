import re

print("*** {n} 사용법 ***")
pattern = re.compile("AD{2}A")  # D가 2개

print(pattern.search("ADA"))  # None
print(pattern.search("ADDA"))  # <re.Match object; span=(0, 4), match='ADDA'>
print(pattern.search("ADDDDA"))  # None

print("\n*** {n,m} 사용법 ***")
pattern = re.compile("AD{2,6}A")  # D가 2개

print(pattern.search("ADA"))  # None
print(pattern.search("ADDA"))  # <re.Match object; span=(0, 4), match='ADDA'>
print(pattern.search("ADDDDA"))  # <re.Match object; span=(0, 6), match='ADDDDA'>

print("\n*** [] 사용법 : [] 문자중에 하나 처음 해당되는거 반환, or의 개념***")
pattern = re.compile("[abcdefgABCDEFG]")

print(pattern.search("a1234"))  # <re.Match object; span=(0, 1), match='a'>
print(pattern.search("z1234"))  # None
print()
pattern = re.compile("[a-g]")  # 연속적일땐 - 처리 가능

print(pattern.search("a1234"))  # <re.Match object; span=(0, 1), match='a'>
print(pattern.search("z1234"))
print()
pattern = re.compile("[a-zA-Z]")  # 연속적일땐 - 처리 가능

print(pattern.search("a1234"))  # <re.Match object; span=(0, 1), match='a'>
print(pattern.search("Z1234"))  # <re.Match object; span=(0, 1), match='Z'>

print()
pattern = re.compile("[a-zA-Z0-9]")  # 연속적일땐 - 처리 가능

print(pattern.search("a1234"))  # <re.Match object; span=(0, 1), match='a'>
print(pattern.search("Z1234"))  # <re.Match object; span=(0, 1), match='Z'>
print(pattern.search("1234"))  # <re.Match object; span=(0, 1), match='1'>

print()
pattern = re.compile("[a-zA-Z0-9]+")  # +: 1개 찾고 무한대이기때문에 전체 문자 반환

print(pattern.search("a1234"))  # <re.Match object; span=(0, 5), match='a1234'>
print(pattern.search("Z1234"))  # <re.Match object; span=(0, 5), match='Z1234'>
print(pattern.search("1234"))  # <re.Match object; span=(0, 4), match='1234'>

print()
pattern = re.compile("[^a-zA-Z0-9]")  # ^뒤에 나온 문자를 제외하고 반환

print(pattern.search("a1234"))  # None
print(pattern.search("Z1234"))  # None
print(pattern.search("1234"))  # None
print(pattern.search("&*%#@!"))  # <re.Match object; span=(0, 1), match='&'>

print()
pattern = re.compile("[가-힣]")  # 한글설정
print(pattern.search("안녕하세요"))  # <re.Match object; span=(0, 1), match='안'>

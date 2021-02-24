import os  # 현재 컴퓨터의 상황을 알아내서 변경이 가능하다.

print("현재 운영체제 : ", os.name)
print("현재 폴더 : ", os.getcwd())
print("현재 폴더 내부의 요소 : ", os.listdir())

with open("original.txt", "w") as f:
    f.write("hello")

# os.rename("original.txt","new.txt") #파일이름 재설정

os.remove("new.txt")  # 파일삭제

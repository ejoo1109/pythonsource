#import pitest  # 클래스 모듈 사용법 : 파일명으로 임포트
from pitest import Test

#obj1 = pitest.Test()  # 파일명.클래스 => 객체생성
obj1 = Test()

print(obj1.solv(5))
print(obj1.sum(5, 5))

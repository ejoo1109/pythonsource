PI = 3.141592


class Test:
    def solv(self, r):
        return PI * (r ** 2)

    def sum(self, a, b):
        return a + b


# 클래스 테스트용 코드
if __name__ == "__main__":
    print(PI)
    a = Test()
    print(a.solv(2))
    print(a.sum(PI, 4.4))

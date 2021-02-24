def add(a, b):
    return a + b


def safe_add(a, b):
    if type(a) != type(b):
        print("더할 수 없습니다.")
        return
    else:
        result = add(a, b)
    return result


# 모듈 테스트 코드
if __name__ == "__main__" : 
    print(add(5, 10.4))
    print(safe_add(5, "6"))
    print(safe_add(5, 6))

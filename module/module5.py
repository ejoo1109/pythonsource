import random

print(random.random()) # 0.0 <= x < 1.0 임의의 수 리턴
print(random.uniform(10,20)) #uniform(min,max) min <= x < max
print(random.randrange(10)) #randrange(max) 0 <= x < max
print(random.choice([1, 2, 3, 4, 5, 6, 7])) #리스트 내부의 요소를 랜덤하게 선택

items = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(items) #원소의 순서를 랜덤하게 섞기
print(items)

print(random.sample([1, 2, 3, 4, 5, 6, 7], k=2))

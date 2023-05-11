import random

rNum = random.randint(1, 10)
print(f'rNum: {rNum}')

# sample을 사용하면 리스트 형태로 데이터가 반환된다.
rNum = random.sample(range(101), 10)
print(f'rNum: {rNum}')
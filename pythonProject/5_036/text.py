# uri = '/Users/boblee/Desktop/제로베이스 강의자료/python.txt/'

# 'w' 모드
# file = open(uri + 'hello.txt','w')
# file.write('hello world')
# file.close()

# # 'a' 모드
# file = open(uri + 'hello.txt','a')
# file.write('\nNice to meet you')
# file.close()

# 'x' 모드
# file = open(uri + 'hello01.txt','x')
# file.write('\nNice to meet you')
# file.close()

# 'r' 모드
# file = open(uri + 'hello01.txt','r')
# str = file.read()
# print(f'str: {str}')
# file.close()

uri = '/Users/boblee/Desktop/제로베이스 강의자료/python.txt/'

def writePrimeNum(n):
    file = open(uri + 'prime_number.txt', 'a')
    file.write(str(n))
    file.write('\n')
    file.close()

inputNum = int(input('0보다 큰 정수 입력:'))
for num in range(2, (inputNum + 1)):
    flag = True
    for n in range(2, num):
        if num % n == 0:
            flag = False
            break

    if flag:
        writePrimeNum(num)

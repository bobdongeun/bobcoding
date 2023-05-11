# n1 = 10; n2 = 10
#
# try:
#     print(n1 / n2)
# except:
#     print('예상치 못한 문제가 발생하였습니다.')
#     print('다른 프로그램은 그대로 실행됩니다..')
# print(n1 + n2)
# print(n1 - n2)
# print(n1 * n2)

nums = []

n = 1
while n < 6:

    try:
        num = int(input('숫자 입력: '))
    except:
        print('예외 발생')
        continue

nums.append(num)
    n += 1

print(f'nums: {nums}')
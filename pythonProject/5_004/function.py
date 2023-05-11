# def great(customer):
#     print('{}님, 안녕하세요.'.format(customer))
#
# great('홍길동')
# great('손흥민')
# great('강호동')
# great('유재석')

# def cal(n1, n2):
#     print(f'{n1} + {n2} = {n1 + n2}')
#     print(f'{n1} - {n2} = {n1 - n2}')
#     print(f'{n1} * {n2} = {n1 * n2}')
#     print(f'{n1} / {n2} = {n1 / n2}')
#
# cal(10, 20)

# def number(*numbers):
#     for number in numbers:
#         print(numbers, end='')
#     print()
#
# number()
# number(10, 20)
# number(10, 20)


def printScore(kor, eng, mat):
    sum = kor + eng + mat
    avg = sum / 3

    print(f'총점 : {sum}')
    print(f'평균 : {round(avg, 2)}')

kor = int(input('국어 점수 입력: '))
eng = int(input('영어 점수 입력: '))
mat = int(input('수학 점수 입력: '))

printScore(kor, eng, mat)
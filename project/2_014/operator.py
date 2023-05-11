# str = 'Hi'
# result = str * 5
#
# print('result: {}'.format(result))
#
# num1 = 20
# num2 = 4
# result = int(num1 / num2)
#
# print('result: {}'.format(type(result)))

kor = int(input('국어 점수: '))
eng = int(input('영어 점수: '))
mat = int(input('수학 점수: '))

total = kor + eng + mat
avg = total / 3

print('국어 점수: {}'.format(kor))
print('영어 점수: {}'.format(eng))
print('수학 점수: {}'.format(mat))
print('합계: {}'.format(total))
print('평균: {}'.format(avg))
print(f'평균: %.2f' % avg)
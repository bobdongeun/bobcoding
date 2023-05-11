# num1 = 10
# num2 = 100
#
# Result = True if num1 > num2 else False
# print('num1 > num2 : {}'.format(Result))
#
# print('num1은 num2보다 크다.') if Result else print('num2는 num1보다 크다.')

# limitSnowAmount = 30
# snowAmount = int(input('적설량 입력(mm): '))
#
# print('적설량 : {}mm, {}'.format(snowAmount, '대설 경보 발령!!')) if snowAmount >= limitSnowAmount \
#     else print('적설량 : {}mm, {}'.format(snowAmount, '대설 경보 해제!!'))

import operator

passScore1 = 60
passScore2 = 70

kor = int(input('국어 점수 : '))
eng = int(input('영어 점수 : '))
mat = int(input('수학 점수 : '))

totalScore = kor + eng + mat
avg = totalScore / 3

print('국어 : PASS') if operator.ge(kor, passScore1) else print('국어 : FAIL')
print('영어 : PASS') if operator.ge(eng, passScore1) else print('영어 : FAIL')
print('수학 : PASS') if operator.ge(mat, passScore1) else print('수학 : FAIL')
print('시험 : PASS') if operator.ge(avg, passScore2) else print('시험 : FAIL')

print('총점 : %d, 평균 : %.2f' %(totalScore, avg))

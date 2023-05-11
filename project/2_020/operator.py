# print('{} and {}'.format(True, True, (True and True)))
# print('{} and {}'.format(True, False, (True and False)))
# print('{} and {}'.format(False, True, (False and True)))
# print('{} and {}'.format(False, False, (False and False)))
#
#
# print('{} or {}'.format(True, True, (True or True)))
# print('{} or {}'.format(True, False, (True or False)))
# print('{} or {}'.format(False, True, (False or True)))
# print('{} or {}'.format(False, False, (False or False)))
#
# print('not {} : {}'.format(True, (not True)))
# print('not {} : {}'.format(False, (not False)))

# age = int(input('나이 입력 : '))
# vaccine = (age < 20) or (age >= 65)
# print('age : {}, result : {}'.format(age, vaccine))

passScore1 = 60
passScore2 = 70
kor = int(input('국어 점수 : '))
eng = int(input('영어 점수 : '))
mat = int(input('수학 점수 : '))
avg = (kor + eng + mat) / 3

avgResult = avg >= passScore2
korResult = kor >= passScore1
engResult = eng >= passScore1
matResult = mat >= passScore1

subjectResult = korResult and engResult and matResult

print('국어 점수 : {}, 결과 : {}'.format(kor, korResult))
print('영어 점수 : {}, 결과 : {}'.format(eng, engResult))
print('수학 점수 : {}, 결과 : {}'.format(mat, matResult))
print('평균 : {}, 결과 : {}'.format(avg, avgResult))
print('과락 결과 : {}'.format(subjectResult))
print('최종 결과 : {}'.format(avgResult and subjectResult))
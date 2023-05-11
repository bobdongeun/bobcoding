# # BMI = 몸무게(kg) / (신장(m) * 신장(m))
#
# weight = input('체중 입력(kg) : ')
# height = input('신장 입력(cm) : ')
#
# if weight.isdigit():
#     weight = int(weight) / 10
#
# if height.isdigit():
#     height = int(height) / 100
#
# print('체중 : {}kg'.format(weight))
# print('신장 : {}m'.format(height))
#
# bmi = weight / (height * height)
# print('BMI: %f' % bmi)

# num1 = 10
# num2 = 20
# print('num1 : {}, num2 : {}'.format(num1, num2))
#
# tempNum = num1
# num1 = num2
# num2 = tempNum
# print('num1 : {}, num2 : {}'.format(num1, num2))

middleExamScore = input('중간 고사 점수 입략: ')
finalExamScore = input('기말 고사 점수 입략: ')

if middleExamScore.isdigit() and finalExamScore.isdigit():
    middleExamScore = int(middleExamScore)
    finalExamScore = int(finalExamScore)

    totalScore = middleExamScore + finalExamScore
    avg = totalScore / 2

    print('총점 : {}, 평균 : {}'.format(totalScore, avg))

else:
    print('잘못 입력 했습니다.')


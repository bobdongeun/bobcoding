# userInputNum1 = int(input('첫 번째 숫자 입력: '))
# userInputNum2 = int(input('두 번째 숫자 입력: '))
#
# print('{} > {} : {} '.format(userInputNum1, userInputNum2, (userInputNum1 > userInputNum2)))
# print('{} < {} : {} '.format(userInputNum1, userInputNum2, (userInputNum1 < userInputNum2)))
# print('{} >= {} : {} '.format(userInputNum1, userInputNum2, (userInputNum1 >= userInputNum2)))
# print('{} <= {} : {} '.format(userInputNum1, userInputNum2, (userInputNum1 <= userInputNum2)))
# print('{} == {} : {} '.format(userInputNum1, userInputNum2, (userInputNum1 == userInputNum2)))
# print('{} != {} : {} '.format(userInputNum1, userInputNum2, (userInputNum1 != userInputNum2)))

maxLength = 5200
maxWidth = 1985

myCarLength = int(input('전장 길이 입력: '))
myCarWidth = int(input('전폭 길이 입력: '))

print('전장 가능 여부 : {}'.format(myCarLength <= maxLength))
print('전폭 가능 여부 : {}'.format(myCarWidth <= maxWidth))
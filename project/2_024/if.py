# passScore = 80
#
# myScore = int(input('점수 입력 : '))
#
# if myScore >= passScore:
#     print('PASS')
#
# else:
#     print('FAIL')

# seniorAge = 65
#
# passengerAge = int(input('나이 입력 : '))
# if passengerAge >= seniorAge:
#     print('무료입니다.')
#
# else:
#     print('유료입니다.')

floatNum = float(input('소수 입력 : '))

if floatNum - int(floatNum) >= 0.5:
    print('올림 : {}'.format(int(floatNum) + 1))

else:
    print('내림 : {}'.format(int(floatNum)))
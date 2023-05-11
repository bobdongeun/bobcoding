import datetime

today = datetime.datetime.today()
day = today.day

limitDust = 150
dustNum = int(input('미세먼지 수치 입력 : '))
carType = int(input('차량 종류 선택 : 1.승용차 \t 2.영업용차'))
carNum = int(input('차량 번호 입력 : '))

print('-' * 30)
print(today)
print('-' * 30)
if dustNum > 150 and carType == 1:
    if day % 2 == (carNum % 2):
        print('차량 2부제 적용')
        print('금일 운행 제한 차량 대상입니다.')
    else:
        print('금일 차량 운행 가능합니다.')
elif dustNum > 150 and carType == 2:
    if day % 5 == (carNum % 5):
        print('차량 5부제 적용')
        print('금일 운행 제한 차량 대상입니다.')
    else:
        print('금일 차량 운행 가능합니다.')
elif dustNum <= limitDust:
    if day % 5 == (carNum % 5):
        print('차량 5부제 적용')
        print('금일 운행 제한 차량 대상입니다.')
    else:
        print('금일 차량 운행 가능합니다.')
print('-' * 30)
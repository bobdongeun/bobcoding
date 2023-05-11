import random
#
# comNum = random.randint(1, 2)
# userNum = int(input('홀/짝 선택: 1.홀 \t 2.짝'))
#
# if comNum == 1 and userNum == 1:
#     print('홀수 빙고!')
# elif comNum == 2 and userNum == 2:
#     print('짝수 빙고!')
# elif comNum == 1 and userNum == 2:
#     print('홀수 실패!')
# elif comNum == 2 and userNum == 1:
#     print('짝수 실패!')1

comNum = random.randint(1, 3)
userNum = int(input('가위, 바위, 보 선택 : 1.가위 \t 2.바위 \t 3.보'))

if (comNum == 1 and userNum == 2) or \
    (comNum == 2 and userNum == 3) or \
    (comNum == 3 and userNum == 1):
    print('컴퓨터 패, 유저 승!')
elif comNum == userNum:
    print('무승부')
else:
    print('컴퓨터 승, 유저 패!')


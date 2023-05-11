# import random
#
# rNum = random.randint(1, 1000)
# tryCnt = 0
# gameFlag = True
# #
#
# while gameFlag:
#     tryCnt += 1
#     userNum = int(input('유저 선택 넘버 : '))
#
#     if rNum == userNum:
#         print('빙고!!')
#         gameFlag = False
#     else:
#         if rNum > userNum:
#             print('rNum이 더 크다!!')
#         else:
#             print('rNum이 더 작다!!')
#
# print('난수 : {}, 시도 횟수 : {}'.format(rNum, tryCnt))

innerTemperture = int(input('실내 온도 입력 : '))

if innerTemperture <= 18:
    print('에어컨 작동 중지')
elif innerTemperture > 18 and innerTemperture <= 22:
    print('에어컨 매우 약 가동!')
elif innerTemperture > 22 and innerTemperture <= 24:
    print('에어컨 약 가동!')
elif innerTemperture > 24 and innerTemperture <= 26:
    print('에어컨 중 가동!')
elif innerTemperture > 26 and innerTemperture <= 28:
    print('에어컨 강 가동!')
elif innerTemperture > 28:
    print('에어컨 매우 강 가동!')

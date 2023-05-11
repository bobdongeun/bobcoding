# def cal(n1, n2):
#     result = n1 + n2
#
#     return result
#
#     print('hello')
#
# returnValue = cal(10, 20)
# print(f'returnValue: {returnValue / 2}')
#

# def devideNum(n):
#
#     if n % 2 == 0:
#         return '짝수'
#     else:
#         return '홀수'
#
# returnVal = devideNum(6)
# print(returnVal)

# def cmToMm(cm):
#     result = cm * 10
#
#     return result
#
# length = float(input('길이(cm)입력 : '))
# returnVal = cmToMm(length)
# print(f'returnVal: {returnVal}mm')

import random

def getOddRandNum():

    while True:
        rNum = random.randint(1, 100)
        if rNum % 2 != 0:
            break

    return rNum

print(f'returnVal : {getOddRandNum()}')
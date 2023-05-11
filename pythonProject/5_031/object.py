# try:
#     inputData = input('input number: ')
#     numInt = int(inputData)
#
# except:
#     print('예외 발생!')
#     print('숫자가 아입니다.')
#
# else:
#     if numInt % 2 == 0:
#         print('짝수입니다.')
#     else:
#         print('홀수입니다.')
#
# finally:
#     print(f'inputData: {inputData}')

eveList = []; oddList = []; floatList = []; dataList = []

n = 1
while n < 6:

    try:
        data = input('input number: ')
        floatNum = float(data)

    except:
        print('예외 발생!')
        print('숫자가 아닙니다.')
        continue

    else:
        if floatNum - int(floatNum) != 0:
            print('float number')
            floatList.append(floatNum)
        else:
            if floatNum % 2 == 0:
                print('even number')
                eveList.append(floatNum)
            else:
                print('odd number')
                oddList.append(floatNum)

        n += 1

    finally:
        dataList.append(data)

print(f'evenList: {eveList}')
print(f'oddList: {oddList}')
print(f'floatList: {floatList}')
print(f'dataList: {dataList}')



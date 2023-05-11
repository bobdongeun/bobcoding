# nums = []
# n = 1
# while n < 6:
#
#     try:
#         num = int(input('숫자 입력: '))
#
#     except:
#         print('예외 발생!')
#         continue
#     else:
#         if num % 2 == 0:
#             nums.append(num)
#             n += 1
#         else:
#             print('홀수입니다.', end='')
#             print('다시 입력하세요.')
#
# print(f'nums: {nums}')

eveList = []; oddList = []; floatList = []

n = 1
while n < 6:

  try:
    num = float(input('input num: '))
  except:
      print('예외 발생!', end='')
      print('다시 입력 해주세요')
      continue

  else:
        if num - int(num) != 0:
            print('float number!')
            floatList.append(num)
        else:
            if num % 2 == 0:
                print('eve number!')
                eveList.append(num)
            else:
                print('odd number!')
                oddList.append(num)

        n += 1

print(f'eveList: {eveList}')
print(f'oddList: {oddList}')
print(f'floatList: {floatList}')
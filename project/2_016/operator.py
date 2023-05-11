# # num1 = 7
# # num2 = 5
# # result = num1 ** num2
# # print('ruesult: {}'.format(result))
#
# # 2의 제곱근
# result = 2 ** (1/2)
# print('result: %.2f' % result)
#
# # 2의 세제곱근
# result = 2 ** (1/3)
# print('result: %.2f' % result)
#
# # 2의 네제곱근
# result = 2 ** (1/4)
# print('result: %.2f' % result)


# import math
#
# print(math.sqrt(5))
#
# print(math.pow(2, 11))

firstMoney = 200
after12Month = int(((firstMoney * 0.01) ** 12) * 100)


print('12개월 후 용돈: {}'.format(after12Month))
str = format(after12Month, ',')
print(str, '원')
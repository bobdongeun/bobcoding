# # 수학 관련 함수
#
# # # 합
# # listVar = [2, 5, 3.14, 58, 10, 2]
# # print(f'sum: {sum(listVar)}')
# #
# # # 최댓값
# # listVar = [2, 5, 3.14, 58, 10, 2]
# # print(f'sum: {max(listVar)}')
# #
# # # 최소값
# # listVar = [2, 5, 3.14, 58, 10, 2]
# # print(f'sum: {min(listVar)}')
# #
# # # 거듭제곱
# # listVar = [2, 5, 3.14, 58, 10, 2]
# # print(f'pow(13, 2): {pow(13, 2)}')
# #
# # # 반올림
# # print(f'{round(3.141592, 2)}')
# # print(f'{round(3.141592, 4)}')
#
#
# import math
#
#
# # 절대값
# print(f'math.fabs(-10) : {math.fabs(-10)}')
# print(f'math.fabs(-0.123344) : {math.fabs(-0.123344)}')
#
# # 올림
# print(f'math.ceil(-5.21) : {math.ceil(-5.21)}')
# print(f'math.ceil(5.21) : {math.ceil(5.21)}')
#
# # 내림
# print(f'math.floor(-5.21) : {math.floor(-5.21)}')
# print(f'math.floor(5.21) : {math.floor(5.21)}')
#
# # 버림
# print(f'math.trunc(-5.21) : {math.trunc(-5.21)}')
# print(f'math.trunc(5.21) : {math.trunc(5.21)}')
#
# # 최대공약수
# print(f'math.gcd(14, 21) : {math.gcd(14, 21)}')
#
# # 팩토리얼
# print(f'math.factoreal(10) : {math.factorial(10)}')
#
# # 제곱근
# print(f'math.sqrt(4) : {math.sqrt(4)}')
# print(f'math.sqrt(21) : {math.sqrt(21)}')
#
#
#

import time

lt = time.localtime()
print(lt)

print(f'lt.tm_year: {lt.tm_year}')
print(f'lt.tm_year: {lt.tm_mon}')
print(f'lt.tm_year: {lt.tm_mday}')
print(f'lt.tm_year: {lt.tm_min}')
print(f'lt.tm_year: {lt.tm_sec}')
print(f'lt.tm_year: {lt.tm_wday}')
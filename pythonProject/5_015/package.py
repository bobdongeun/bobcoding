# import sys
#
# for path in sys.path:
#     print(path)

# from calculator import cal
# print(f'cal.add(10, 20): {cal.add(10, 20)}')
# print(f'cal.sub(10, 20): {cal.sub(10, 20)}')
# print(f'cal.mul(10, 20): {cal.mul(10, 20)}')
# print(f'cal.div(10, 20): {cal.div(10, 20)}')

from divisor_mod import mod

print(f'10의 약수: {mod.divisor(10)}')
print(f'50까지의 소수: {mod.prime_num(50)}')
# # 빈 문자 -> 논리형 빈 문자는 False
# var = ''
# print(var)
# print(type(var))
#
# var = bool(var)
# print(var)
# print(type(var))
#
# # 공백 -> 논리형 공백 문자는 True
# var = ' '
# print(var)
# print(type(var))
#
# var = bool(var)
# print(var)
# print(type(var))

# 문자 -> 논리형 -> 산술 연산
var1 = 'True'
var2 = 'False'
print(type(var1))
print(type(var2))

var1 = bool(var1)
var2 = bool(var2) # 왜 False가 아닐까? 공백 문자 이므로 True로 인식됨
print(var1)
print(var2)
print(type(var1))
print(type(var2))

print(var1 + var2)

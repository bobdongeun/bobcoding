# radius = int(input('반지름(cm) 입력 : '))
# circleArea = radius * radius * 3.14
# circleRound = 2 * 3.14 * radius
# print('원의 넓이 : %.3f cm' % circleArea)
# print('원의 넓이 : %.3f cm' % circleRound)

name = input('이름 입력 : ')
mail = input('메일 입력 : ')
id = input('아이디 입력 : ')
pw = input('비밀번호 입력 : ')
privateNum1 = input('주민번호 앞자리 입력 : ')
privateNum2 = input('주민번호 뒷자리 입력 : ')
address = input('주소 입력 : ')

print('-' * 30)
print(f'이름 : {name}')
print(f'메일 : {mail}')
print(f'아이디 : {id}')
pwStar = '*' * len(pw)
print(f'비밀번호 : {pwStar}')
privateNumStar = privateNum2[0] + ('*' * 6)
print(f'주민번호 : {privateNum1} - {privateNumStar}')
print(f'주소 : {address}')
print('-' * 30)
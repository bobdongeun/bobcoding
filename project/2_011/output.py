userName = 'Hong gil dong'
print(userName)

userAge = 20
print(userAge)

# print('User name: ', userName)
# print('User age: ', userAge)
# print('User name: ', userName, ', User age: ', userAge)
#
# print('3 * 5 = ', end='') # end=''을 통해서 자동 개행 방지
# print(3 * 5)

# format 문자열을 이용한 데이터 출력
print(f'User name : {userName}')
print(f'User age : {userAge}')
print(f'User name : \t{userName}, \nUser age : {userAge}') # \n 개행 \t 띄어쓰기

width = int(input('가로 길이 입력: '))
height = int(input('세로 길이 입력: '))

triangle = width * height / 2
print(f'width : {width}, height : {height}, triangle : {triangle}')
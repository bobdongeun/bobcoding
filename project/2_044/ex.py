# language = int(input('언어 선택(choose your language : 1.한국어 \t 2.English'))
#
# if language == 1:
#     menu = int(input('1.샌드위치 \t 2.햄버거 \t 3.쥬스 \t 4.커피 \t 5.아이스크림'))
#
# elif language == 2:
#     menu = int(input('1.Sandwich \t 2.Hamburger \t 3.Juice \t 4.Coffee \t 5.Ice cream'))
#
# print(menu)

import datetime

today = datetime.datetime.today()

myAge = input('나이 입력: ')
if myAge.isdigit():

    afterAge = 100 - int(myAge)
    myHundred = today.year + afterAge

    print('{}년 ({}년후)에 100살 ㅠㅠ'.format(myHundred, afterAge))

else:
    print('잘 못 입력했습니다.')
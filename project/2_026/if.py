# # exampleScore = int(input('시험 성적 입력: '))
# # grades = ''
# #
# # if exampleScore >= 90:
# #     grades = 'A'
# # elif exampleScore >= 80:
# #     grades = 'B'
# # elif exampleScore >= 70:
# #     grades = 'C'
# # elif exampleScore >= 60:
# #     grades = 'D'
# # else:
# #     grades = 'F'
# #
# # print('성적 : {} \t 학점 : {}'.format(exampleScore, grades))
#
# print('계절 : 봄, 여름, 가을, 겨울')
# season = input('계절 입력 : ')
#
# if season == '봄':
#     print('{} : {}'.format('봄', 'Spring'))
# elif season == '여름':
#     print('{} : {}'.format('여름', 'Summer'))
# elif season == '가을':
#     print('{} : {}'.format('가을', 'Fall'))
# elif season == '겨울':
#     print('{} : {}'.format('겨울', 'Winter'))
# else:
#     print('검색할 수 없습니다.')

print('1.카페라떼(3.5) \t 2.에스프레소(3.0) \t 3.아메리카노(2.0) \t 4.곡물라뗴(4.0) \t 5.밀크티(4.3)')
userSelect = int(input('메뉴 선택 : '))

print('-' * 30)
if userSelect == 1:
    print('메뉴 : {} \n가격 : {}'.format('카페라떼','3,500원'))
elif userSelect == 2:
    print('메뉴 : {} \n가격 : {}'.format('에스프레소', '3,000원'))
elif userSelect == 3:
    print('메뉴 : {} \n가격 : {}'.format('아메리카노', '2,000원'))
elif userSelect == 4:
    print('메뉴 : {} \n가격 : {}'.format('곡물라떼', '4,000원'))
elif userSelect == 5:
    print('메뉴 : {} \n가격 : {}'.format('밀크티', '4,300원'))
else:
    print('없는 메뉴 입니다.')
print('-' * 30)
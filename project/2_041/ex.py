# userMessage = input('메시지 입력: ')
# print('메시지 문자열 길이 : {}'.format(len(userMessage)))

# article = '파이썬[3](영어: Python)은 1991년[4] 네덜란드계 소프트웨어 엔지니어인 귀도 반 로섬[5]이 발표한 고급 프로그래밍 언어로, ' \
#           '플랫폼에 독립적이며 인터프리터식, 객체지향적, 동적 타이핑(dynamically typed) 대화형 언어이다. ' \
#           '파이썬이라는 이름은 귀도가 좋아하는 코미디인〈Monty Python\'s Flying Circus〉에서 따온 것이다.' \
#           '이름에서 고대신화에 나오는 커다란 뱀을 연상하는 경우도 있겠지만 이와는 무관하다. 다만 로고에는 뱀 두마리가 형상화되어 있다.'
#
# strIdx = article.find('객체지향')
# print('객체지향 문자열 위치: {}'.format(strIdx))

width = float(input('가로 길이 입력 : '))
height = float(input('세로 길이 입력 : '))
triangle = width * height / 2
square = width * height

print('-' * 25)
print('삼각형 넓이 : %.2f' % triangle)
print('사각형 넓이 : %.2f' % square)
print('-' * 25)
# if 10 > 5:
#     print('10은 5보다 크다')
#
# num1 = 10
# num2 = 20
#
# if num1 <= num2:
#     print('num1은 num2보다 작거나 같다.')

# kor = int(input('국어 점수 : '))
# eng = int(input('영어 점수 : '))
# mat = int(input('수학 점수 : '))
#
# avg = (kor + eng + mat) / 3
# print('평균 : {}'.format(avg))
#
# if avg >= 90:
#     print('참 잘했어요~')

highTemperture = 28
lowTemperture = 20

innerTemperture = int(input('실내 온도 : '))

if innerTemperture >= highTemperture:
    print('에어컨 작동!!')

if innerTemperture <= lowTemperture:
    print('난방 작동!!')
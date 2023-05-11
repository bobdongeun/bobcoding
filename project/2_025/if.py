# rainPercent = int(input('비올 확률 입력 : '))
# minRainPercent = 55
#
# if rainPercent >= minRainPercent:
#     print('우산을 챙기세요.')
#
# else:
#     print('양산을 챙기세요.')

lowTemperture = int(input('최저 기온 입력: '))
highTemperture = int(input('최고 기온 입력: '))
distance = highTemperture - lowTemperture

if distance >= 11:
    print('일교차: {}도'.format(distance),
          '감기 조심하세요~')

else:
    print('일교차: {}도'.format(distance),
          '산책하기 좋은 날씨입니다.')
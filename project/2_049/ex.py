# age = int(input('나이 입력 : '))
#
# if age <= 19 or age >= 60:
#     end = int(input('출생 연도 끝자리 입력 : '))
#     if end == 1 or end == 6:
#         print('월요일 접종 가능')
#     elif end == 2 or end == 7:
#         print('화요일 접종 가능')
#     elif end == 3 or end == 8:
#         print('수요일 접종 가능')
#     elif end == 4 or end == 9:
#         print('목요일 접종 가능')
#     elif end == 5 or end == 0:
#         print('금요일 접종 가능')
#
# else:
#     print('하반기 일정을 확인하세요.')

byInch = 0.039
lengthMM = int(input('길이(mm)입력 : '))
lengthInch = lengthMM * byInch

print('{}mm -> {}inch'.format(lengthMM, lengthInch))
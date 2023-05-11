korAvg = 85; engAvg = 82; matAvg = 89
sciAvg = 75; hisAvg = 94
totalAvg = korAvg + engAvg + matAvg + sciAvg +hisAvg
avgAvg = int(totalAvg / 5)

kor = int(input('국어 점수 : '))
eng = int(input('영어 점수 : '))
mat = int(input('수학 점수 : '))
sci = int(input('과학 점수 : '))
his = int(input('국사 점수 : '))

total = kor + eng + mat + sci + his
avg = int(total / 5)

korGap = kor - korAvg
engGap = eng - engAvg
matGap = mat - matAvg
sciGap = sci - sciAvg
hisGap = his - hisAvg

totalGap = total - totalAvg
avgGap = avg - avgAvg

print('-' * 70)
print('총점 : {}({}), 평균 : {}({})'.format(total, totalGap, avg, avgGap))
print('국어 : {}({}), 영어 : {}({}), 수학 : {}({}), 과학 : {}({}), 국사 : {}({})'.format(
    kor, korGap, eng, engGap, mat, matGap, sci, sciGap ,his, hisGap))
print('-' * 70)

str = '+' if korGap > 0 else '-'
print('국어 편차 : {}({})'.format(str * abs(korGap), korGap))
str = '+' if engGap > 0 else '-'
print('영어 편차 : {}({})'.format(str * abs(engGap), engGap))
str = '+' if matGap > 0 else '-'
print('수학 편차 : {}({})'.format(str * abs(matGap), matGap))
str = '+' if sciGap > 0 else '-'
print('과학 편차 : {}({})'.format(str * abs(sciGap), sciGap))
str = '+' if hisGap > 0 else '-'
print('국사 편차 : {}({})'.format(str * abs(hisGap), hisGap))

str = '+' if totalGap > 0 else '-'
print('총점 편차 : {}({})'.format(str * abs(totalGap), totalGap))
str = '+' if avgGap > 0 else '-'
print('평귱 편차 : {}({})'.format(str * abs(avgGap), avgGap))
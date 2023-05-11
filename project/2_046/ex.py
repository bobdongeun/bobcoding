kor = int(input('국어 점수 입력: '))
eng = int(input('영어 점수 입력: '))
mat = int(input('수학 점수 입력: '))
total = kor + eng + mat
avg = total / 3

maxScore = kor
maxSubject = '국어'
if eng > maxScore:
    maxScore = eng
    maxSubject = '영어'

if mat > maxScore:
    maxScore = mat
    maxSubject = '수학'

minScore = kor
minSubject = '국어'
if eng < minScore:
    minScore = eng
    minSubject = '영어'

if mat < minScore:
    minScore = mat
    minSubject = '수학'

distance = maxScore - minScore

print('총점: {}'.format(total))
print('평균: %.2f' % avg)
print('-' * 30)
print('최고 점수 과목(점수) : {}({})'.format(maxSubject, maxScore))
print('최저 점수 과목(점수) : {}({})'.format(minSubject, minScore))
print('최고, 최저 점수 차이 : {}'.format(distance))
print('-' * 30)
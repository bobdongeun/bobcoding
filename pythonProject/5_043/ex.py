# def formatedNum(n):
#     return format(n, ',')
#
# def recursion(n):
#
#     if n == 1:
#         return n
#
#     return n * recursion(n-1)
#
# inputNum = int(input('input number: '))
# print(formatedNum(recursion(inputNum)))
#
def formatedNum(n):
    return format(n, ',')

#단리
def singleRageCal(m, t, r):

    totalMoney = 0
    totalRateMony = 0

    for i in range(t):
        totalRateMony += m * (r * 0.01)

    totalMoney = m + totalRateMony
    return int(totalMoney)

# 월 복리

def multiRateCal(m, t, r):

    t = t * 12
    rpm = (r / 12) * 0.01

    totalMoney = m

    for i in range(t):
        totalMoney += totalMoney * rpm
    return int(totalMoney)

print('[단리 계산기] ')
print('=' * 30)
money = int(input('예치금(원): '))
term = int(input('기간(년): '))
rate = int(input('연이율(%): '))
print('-' * 30)
print(f'{term}년 후 총 수령액: {formatedNum(singleRageCal(money, term, rate))}')
print('=' * 30)

print('[월 복리 계산기] ')
print('=' * 30)
print(f'{term}년 후 총 수령액: {formatedNum(multiRateCal(money, term, rate))}')
print('=' * 30)
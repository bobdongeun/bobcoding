childPrice = 18000
infantPrice = 25000
adultPrice = 50000
specialDC = 50

def formatedNum(n):
    return format(n, ',')
def printAirplaneRecipt(c1, c2, i1, i2, a1, a2):
    print('=' * 50)
    cp = c1 * childPrice
    cp_dc = int(c2 * childPrice * 0.5)
    print(f'유아: {c1}명 요금: {formatedNum(cp)}원')
    print(f'할인 대상 유아: {c2}명 요금: {formatedNum(cp_dc)}원')

    ip = i1 * infantPrice
    ip_dc = int(i2 * infantPrice * 0.5)
    print(f'소아: {i1}명 요금: {formatedNum(ip)}원')
    print(f'할인 대상 소아: {formatedNum(i2)}명 요금: {formatedNum(ip_dc)}원')

    ap = a1 * adultPrice
    ap_dc = int(a2 * adultPrice* 0.5)
    print(f'성인: {a1}명 요금: {formatedNum(ap)}원')
    print(f'할인 대상 성인: {a2}명 요금: {formatedNum(ap_dc)}원')
    print('=' * 50)
    print(f'Total: {c1 + c2 + i1 + i2 + a1 + a2}명')
    print(f'Total: {formatedNum(cp + cp_dc + ip + ip_dc + ap + ap_dc)}원')
    print('=' * 50)


childCnt = int(input('유아 입력 : '))
childDCCnt = int(input('할인 유아 입력 : '))

infantCnt = int(input('소아 입력 : '))
infantDCCnt = int(input('할인 소아 입력 : '))

adultCnt = int(input('성인 입력 : '))
adultDCCnt = int(input('할인 성인 입력 : '))

printAirplaneRecipt(childCnt, childDCCnt,
                    infantCnt, infantDCCnt,
                    adultCnt, adultDCCnt)

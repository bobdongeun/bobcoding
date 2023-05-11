# 약수 구하는 공식
def divisor(inputNum):
    result = []
    for i in range(1, (inputNum + 1)):
        if inputNum % i == 0:
            result.append(i)

    return result

# 소수 구하는 공식
def prime_num(inputNum):
    result = []
    for i in range(2, (inputNum + 1)):
        flag = True
        for n in range(2, i):
            if i % n == 0:
                flag = False
                break

        if flag:
            result.append(i)
    return result
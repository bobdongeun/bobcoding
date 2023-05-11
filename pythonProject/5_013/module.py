import uniConversion as uc

if __name__ == '__main__':
    inputNum = int(input('길이(cm) 입력: '))
    returnVal = uc.cmToMm(inputNum)
    print(f'returnVal: {returnVal}mm')

    returnVal = uc.cmToM(inputNum)
    print(f'returnVal: {returnVal}m')

    returnVal = uc.cmToFt(inputNum)
    print(f'returnVal: {returnVal}ft')

    returnVal = uc.cmToInch(inputNum)
    print(f'returnVal: {returnVal}inch')
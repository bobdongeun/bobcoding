# def fun1():
#     print('fun1 호출!')
#     fun2()
#     print('fun4 호출!')
# def fun2():
#     print('fun2 호출!')
#     fun3()
# def fun3():
#     print('fun3 호출!')
#
# fun1()

def gugudan2():
    for i in range(1, 10):
        print('2 * {} = {}'.format(i, 2* i))
        gugudan3()

def gugudan3():
    for i in range(1, 10):
        print('3 * {} = {}'.format(i, 3 * i))
        gugudan4()

def gugudan4():
    for i in range(1, 10):
        print('4 * {} = {}'.format(i, 4 * i))
        gugudan5()

def gugudan5():
    for i in range(1, 10):
        print('5 * {} = {}'.format(i, 5 * i))

gugudan2()
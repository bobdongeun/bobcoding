# class NotUseZeroException(Exception):
#
#     def __init__(self, n):
#         super().__init__(f'{n}은 사용할 수 없습니다.')
#
#
# def divCal(n1, n2):
#
#     if n2 == 0 :
#         raise NotUseZeroException(n2)
#
#     else:
#         print(f'n1 / n2 = {n1 / n2}')
#
#
# num1 = int(input('input num1 : '))
# num2 = int(input('input num2 : '))
#
# try:
#     divCal(num1, num2)
# except NotUseZeroException as e:
#     print(e)

class PasswordLenShortException(Exception):

    def __init__(self, str):
        super().__init__(f'{str}: 길이 5미만')


class PasswordLenLongException(Exception):

    def __init__(self, str):
        super().__init__(f'{str}: 길이 10초과')


class PasswordWrongException(Exception):

    def __init__(self, str):
        super().__init__(f'{str}: 잘못된 비밀번호')

password = input('input password : ')

try:
    if len(password) < 5:
        raise PasswordLenShortException(password)

    elif len(password) > 10:
        raise PasswordLenLongException(password)

    elif password != 'admin1234':
        raise PasswordWrongException(password)

    elif password == 'admin1234':
        print('로그인 성공!')

except PasswordLenShortException as e1:
    print(e1)

except PasswordLenLongException as e2:
    print(e2)

except PasswordWrongException as e3:
    print(e3)

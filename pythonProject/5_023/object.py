# # class Calculator:
# #
# #     def __init__(self, n1, n2):
# #         print('[Calculator] __init__() called')
# #         self.num1 = n1
# #         self.num2 = n2
# #
# # cal = Calculator(10, 20)
# #
# # print(f'cal.num1: {cal.num1}')
# # print(f'cal.num2: {cal.num2}')
#
# class Calculator:
#
#     def __init__(self, n):
#         print('[Calculator] __init__() called')
#         self.num1 = n
#         self.num2 = 20
#
# cal = Calculator(100)
#
# print(f'cal.num1: {cal.num1}')
# print(f'cal.num2: {cal.num2}')

class P_Class:

    def __init__(self, n1, n2):
        print('[P_Class] __init__() called')

        self.num1 = n1
        self.num2 = n2


class C_Class(P_Class):

    def __init__(self, cNum1, cNum2):
        print('[C_Class] __init__() called')

        # P_Class.__init__(self, cNum1, cNum2)
        super().__init__(cNum1, cNum2)

        self.cNum1 = cNum1
        self.cNum2 = cNum2

cls = C_Class(10, 20)


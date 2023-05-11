# class Car01:
#
#     def drive(self):
#         print('drive() method called')
#
#
# class Car02:
#
#     def turbo(self):
#         print('turbo() method called')
#
#
# class Car03:
#
#     def fly(self):
#         print('fly() method called')
#
# class Car(Car01, Car02, Car03):
#
#     def __init__(self):
#         pass
#
# myCar = Car()
# myCar.drive()
# myCar.turbo()
# myCar.fly()

class BasicCal:

    def add(self, n1, n2):
        return n1 + n2

    def sub(self, n1, n2):
        return n1 - n2

    def mul(self, n1, n2):
        return n1 * n2

    def div(self, n1, n2):
        return n1 / n2

class DeveloperCal:

    def mod(self, n1, n2):
        return n1 % n2

    def floor(self, n1, n2):
        return n1 // n2

    def exp(self, n1, n2):
        return n1 ** n2

class MyCal(BasicCal, DeveloperCal):

    def __init__(self):
        pass

cal = MyCal()

print(f'cal.add(10, 20): {cal.add(10, 20)}')
print(f'cal.exp(10, 20): {cal.exp(2, 4)}')
print(f'cal.floor(10, 20): {cal.floor(10, 20)}')
print(f'cal.mul(10, 20): {cal.mul(10, 20)}')

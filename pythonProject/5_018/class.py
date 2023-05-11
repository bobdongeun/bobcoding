# class Car:
#
#     def __init__(self, col, len):
#         self.color = col
#         self.length = len
#
#     def doStop(self):
#         print('STOP!')
#
#     def doStart(self):
#         print('START!')
#
#     def printCarInfo(self):
#         print(f'self.color: {self.color}')
#         print(f'self.length: {self.length}')
#
# car1 = Car('red', 200)
# car2 = Car('blue', 300)
#
# car1.printCarInfo()
# car2.printCarInfo()

class Airplane:

    def __init__(self, c, len, wgt):
        self.color = c
        self.length = len
        self.weight = wgt

    def fly(self):
        print('이륙!!')

    def arrive(self):
        print('착륙!!')

    def printAirplaneInfo(self):
        print(f'self.color: {self.color}')
        print(f'self.length: {self.length}')
        print(f'self.weight: {self.weight}')

airplane1 = Airplane('blue', 1200, '1t')
airplane2 = Airplane('red', 1100, '1.5t')

airplane1.printAirplaneInfo()
airplane2.printAirplaneInfo()
Airplane.fly(Airplane)
Airplane.arrive(Airplane)

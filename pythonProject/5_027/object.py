from abc import ABCMeta
from abc import abstractmethod
#
# class AirPlane(metaclass=ABCMeta):
#
#     @abstractmethod
#     def flight(self):
#         pass
#
#     def forward(self):
#         print('전진')
#
#     def backward(self):
#         print('후진')
#
# class AirLiner(AirPlane):
#
#     def __init__(self, c):
#         self.color = c
#
#     def flight(self):
#         print('시속 400km/h 비행')
#
# class FlighterPlane(AirPlane):
#
#     def __init__(self, c):
#         self.color = c
#
#     def flight(self):
#         print('시속 700km/h로 비행')
#
# al = AirLiner('red')
# al.backward()
# al.flight()
# al.forward()
#
# fl = FlighterPlane('red')
# fl.backward()
# fl.flight()
# fl.forward()

class BasicCal(metaclass=ABCMeta):

    @abstractmethod
    def add(self, n1, n2):
        pass

    @abstractmethod
    def sub(self, n1, n2):
        pass

    @abstractmethod
    def mul(self, n1, n2):
        pass

    @abstractmethod
    def div(self, n1, n2):
        pass

class DeveloperCal(BasicCal):

    def add(self, n1, n2):
        print(n1 + n2)

    def sub(self, n1, n2):
        return n1 - n2

    def mul(self, n1, n2):
        return n1 * n2

    def div(self, n1, n2):
        return n1 / n2

    def mod(self, n1, n2):
        return n1 % n2

    def floor(self, n1, n2):
        return n1 // n2

    def exp(self, n1, n2):
        return n1 ** n2

cal = DeveloperCal()

print(f'cal.add(10, 20): {cal.add(10, 20)}')
print(f'cal.exp(10, 20): {cal.exp(2, 4)}')
print(f'cal.floor(10, 20): {cal.floor(10, 20)}')
print(f'cal.mul(10, 20): {cal.mul(10, 20)}')

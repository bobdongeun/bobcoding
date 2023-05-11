# class NormalCar:
#
#     def drive(self):
#         print(f'[Normal Car] drive() called')
#
#     def back(self):
#         print(f'[Normal Car] back() called')
#
# class TurboCar(NormalCar):
#
#     def turbo(self):
#         print(f'[Turbo Car] turbo() called')
#
# myTurbo = TurboCar()
# myTurbo.turbo()
# myTurbo.drive()
# myTurbo.back()

class CalSuper:

    def add(self, n1, n2):
        return n1 + n2

    def sub(self, n1, n2):
        return n1 - n2

class CalChild(CalSuper):

    def mul(self, n1, n2):
        return n1 * n2

    def div(self, n1, n2):
        return n1 / n2

myCal = CalChild()

print(myCal.add(10, 20))
print(myCal.sub(10, 20))
print(myCal.mul(10, 20))
print(myCal.div(10, 20))
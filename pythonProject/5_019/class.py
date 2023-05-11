# class NewGenerationPC:
#
#     def __init__(self, name, cpu, memory, ssd):
#         self.name = name
#         self.cpu = cpu
#         self.memory = memory
#         self.ssd = ssd
#
#     def doExcel(self):
#         print('EXCEL RUN')
#
#     def doPhotoshop(self):
#         print('PHOTOSHOP RUN')
#
#     def printPCInfo(self):
#         print(f'self.name: {self.name}')
#         print(f'self.cpu: {self.cpu}')
#         print(f'self.memory: {self.memory}')
#         print(f'self.ssd: {self.ssd}')
#
# myPC = NewGenerationPC('myPC', 'i5', '16GB', '1TB')
# myPC.printPCInfo()
#
# myFriendPC = NewGenerationPC('myFriendPC', 'i7', '32GB', '2TB')
# myFriendPC.printPCInfo()
#
# myPC.cpu = 'i9'
# myPC.memory = '512GB'
# myPC.ssd = '3TB'
# myPC.printPCInfo()

class Calculator:

    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.result = 0

    def add(self):
        self.result = self.num1 + self.num2
        return self.result

    def sub(self):
        self.result = self.num1 - self.num2
        return self.result

    def mul(self):
        self.result = self.num1 * self.num2
        return self.result

    def div(self):
        self.result = self.num1 / self.num2
        return self.result

cal = Calculator()
cal.num1 = 10
cal.num2 = 20

print(f'cal.add: {cal.add()}')
print(f'cal.sub: {cal.sub()}')
print(f'cal.mul: {cal.mul()}')
print(f'cal.div: {cal.div()}')

cal.num1 = 3
cal.num2 = 5

print(f'cal.add: {cal.add()}')
print(f'cal.sub: {cal.sub()}')
print(f'cal.mul: {cal.mul()}')
print(f'cal.div: {cal.div()}')

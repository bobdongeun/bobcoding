# class Robot:
#
#     def __init__(self, color, height, weight):
#         self.color = color
#         self.height = height
#         self.weight = weight
#
#     def printRobotInfo(self):
#         print(f'color: {self.color}')
#         print(f'height: {self.height}')
#         print(f'weight: {self.weight}')
#
# rb1 = Robot('red', 200, 80)
# rb2 = Robot('green', 300, 120)
# rb3 = rb1
# rb3.printRobotInfo()
# rb1.printRobotInfo()
# rb2.printRobotInfo()
#
# rb1.color = 'grey'
# rb1.height = 250
# rb1.weight = 150
# rb1.printRobotInfo()
# rb3.printRobotInfo()

scores = [
    int(input('국어 점수 입력: ')),
    int(input('영어 점수 입력: ')),
    int(input('수학 점수 입력: '))
]

print(scores)

copyScore = scores.copy()

for idx, score in enumerate(copyScore):
    result = score * 1.1
    copyScore[idx] = 100 if result > 100 else result

print(f'이전 평귱: {round(sum(scores) / len(scores), 2)}')
print(f'이후 평귱: {round(sum(copyScore) / len(copyScore), 2)}')
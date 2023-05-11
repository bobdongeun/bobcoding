# def calculator(n1, n2):
#     return n1 + n2
#
# returnVAL = calculator(10, 20)
# print(returnVAL)

# calculator = lambda n1, n2: n1 + n2  # 함수 선언과 같음
#
# returnVAL = calculator(10, 20)
# print(f'returnVAL: {returnVAL}')

triangle = lambda n1, n2: n1 * n2 / 2
square = lambda n1, n2: n1 * n2
circle = lambda r: r * r * 3.14

width = int(input('가로 길이 입력: '))
height = int(input('세로 길이 입력: '))
radius = int(input('반지름 길이 입력: '))

triangleVal = triangle(width, height)
squareVal = square(width, height)
circleVal = circle(radius)

print(f'삼각형 넓이 : {triangleVal}')
print(f'사각형 넓이 : {squareVal}')
print(f'워 넓이 : {circleVal}')


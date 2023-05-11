# 거리(km) = 시간(h) * 속도(km/h)

def getDistance(speed, hour, minute):
    distance = speed * (hour + minute / 60)
    return distance

def getTime(speed, distance):
    time = distance / speed
    print(f'time: {time}')
    h = int(time)
    m = int((time - h) * 100 * 60 / 100)

    return [h, m]

# print('-' * 70)
# s = float(input('속도(km/h) 입력: '))
# h = float(input('시간(h) 입력: '))
# m = float(input('분(m) 입력: '))
# d = getDistance(s, h, m)
# print(f'{s}(km/h)속도로 {h}시간 {m}분 동안 이동한 거리: {d}km')
# print('-' * 70)

# 100:75=60:x -> x = (75*60) / 100
print('-' * 70)
s = float(input('속도(km/h) 입력: '))
d = float(input('거리(km) 입력: '))
t = getTime(s, d)
print(f'{s}(km/h)속도로 {d}km 동안 이동한 거리: {t[0]}시간 {t[1]}분')
print('-' * 70)

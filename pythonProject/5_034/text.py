# file = open('/Users/boblee/Desktop/제로베이스 강의자료/python.txt/test.txt', 'w')
#
# strCnt = file.write('hello python!')
# print(f'strCnt: {strCnt}')
# file.close()

import time

lt = time.localtime()

dateStr = '[' + str(lt.tm_year) + '년' + \
            str(lt.tm_mon) + '월' + str(lt.tm_mday) + '일]'

todaySchedule = input('오늘 일정: ')

file = open('/Users/boblee/Desktop/제로베이스 강의자료/python.txt/test.txt', 'w')
file.write(dateStr + todaySchedule)

file.close()
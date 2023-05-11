# file = open('/Users/boblee/Desktop/제로베이스 강의자료/python.txt/test.txt', 'r')
#
# str = file.read()
# print(f'str: {str}')
# file.close()

# import time
#
# lt = time.localtime()

# dateStr = '[' + str(lt.tm_year) + '년' + \
#             str(lt.tm_mon) + '월' + str(lt.tm_mday) + '일]'

# dateStr = '[' + time.strftime('%Y-%m-%d %H:%M:%S %p') + ']'
#
# todaySchedule = input('오늘 일정: ')
#
# file = open('/Users/boblee/Desktop/제로베이스 강의자료/python.txt/test.txt', 'w')
# file.write(dateStr + todaySchedule)
#
# file.close()



file = open('/Users/boblee/Desktop/제로베이스 강의자료/python.txt/test.txt', 'r')

str = file.read()
print(f'str: {str}')

file.close()


str = str.replace('Python', '파이썬', 2)
print(f'str: {str}')

file = open('/Users/boblee/Desktop/제로베이스 강의자료/python.txt/test.txt', 'w')
file.write(str)
file.close()
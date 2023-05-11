# speed = int(input('속도 입력 : '))
#
# if speed > 50:
#     print('속도 위반!! 과태료 50,000원 부과')
#
# else:
#     print('안전속도 준수')

msg = input('메시지 입력 : ')
lenMsg = len(msg)
msgPrice = 50

if lenMsg > 10:
    msgPrice = 100
    print('MMS 발송')

else:
    msgPrice = 50
    print('MMS 발송')

print('메시지 길이 : {}'.format(lenMsg))
print('메시지 요금 : {}'.format(msgPrice))
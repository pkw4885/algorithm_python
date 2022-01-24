dNum = 30

print('2진수 : {}'.format(bin(dNum)))
print('8진수 : {}'.format(oct(dNum)))
print('16진수 : {}'.format(hex(dNum)))

print('2진수 타입 : {}'.format(type(bin(dNum))))
print('8진수 타입 : {}'.format(type(oct(dNum))))
print('16진수 타입 : {}'.format(type(hex(dNum))))

print('{0:#b},{0:#o},{0:#x}'.format(dNum))

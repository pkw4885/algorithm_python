# 최대공배수 구하기 2

num1 = int(input('1보다 큰 정수 입력 : '))
num2 = int(input('1보다 큰 정수 입력 : '))
num3 = int(input('1보다 큰 정수 입력 : '))


for i in range(1, (num1 + 1)) :
    if num1 % i == 0 and num2 % i == 0:
        print('공약수 : {}'.format(i))
        maxNum = i

print('{}와 {}의 최대공약수 : {}'.format(num1, num2, maxNum))

minNum = (num1 * num2) // maxNum

print('{}와 {}의 최소공배수 : {}'.format(num1, num2, minNum))

newNum = minNum
for i in range(1, (newNum + 1)) :
    if newNum % i == 0 and num3 % i == 0:
        maxNum = i

print('{}와 {}와 {}의 최대공약수 : {}'.format(num1, num2, num3, maxNum))

minNum = (newNum * num3) // maxNum
print('{}와 {}와 {}의 최소공배수 : {}'.format(num1, num2, num3, minNum))



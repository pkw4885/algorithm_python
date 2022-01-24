# 최대 공약수 구하기 2
# 유클리즈 호제법 사용하기

num1 = int(input('1보다 큰 정수 입력 : '))
num2 = int(input('1보다 큰 정수 입력 : '))

temp1 = num1
temp2 = num2

while temp2 > 0:
    temp = temp2
    temp2 = temp1 % temp2
    temp1 = temp

print('{}, {}의 최대공약수 : {}'.format(num1, num2, temp1))

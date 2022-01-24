inputN1 = int(input('첫번째 항 입력 : '))
inputD = int(input('공차 입력 : '))
inputN = int(input('몇 번 째 항을 알고 싶은가요?'))

n=1
value = 0
valueN = inputN1

print('{}번째 항의 값 : {}'.format(n, inputN1))
while n < inputN:
    value = value + valueN + inputD
    valueN = 0
    n += 1
    print('{}번째 항의 값 : {}'.format(n, value))

sum = n * (inputN1 + value) / 2

print('수열의 합 : {}'.format(sum))

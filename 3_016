#등비수열

inputN1 = int(input('첫 항 입력하세요. '))
inputR = int(input('공비를 입력하세요. '))
inputN = int(input('알고 싶은 n 번째 항은? '))

n = 1
value = 1
valueN1 = inputN1
print('{}항은 {}입니다'.format(1, inputN1))
sum = 0

while n < inputN:
    value = value * valueN1 * inputR
    valueN1 = 1
    n += 1
    sum = sum + value
    print('{}항은 {}입니다'.format(n, value))

print('총 합은 {}'.format(sum))

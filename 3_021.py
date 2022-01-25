#피보나치 수열

inputN = int(input('2보다 큰 n 입력 : '))
valuePreN1 = int(input('첫번째항 입력 : '))
valuePreN2 = int(input('두번째항 입력 : '))

valueN=0
sumN = valuePreN1 + valuePreN2
n1 = valuePreN1
n2 = valuePreN2

n=1
while n<=inputN:
    if n==1:
        print('피보나치 수열의 {}번째 항은 {}입니다'.format(n,n1))
    elif n==2:
        print('피보나치 수열의 {}번째 항은 {}입니다'.format(n,n2))
    else:
        valueN = n1 + n2
        tmp = valueN
        n1 = n2
        n2 = tmp
        sumN += valueN
        print('피보나치 수열의 {}번쨰 항은 {}입니다'.format(n,valueN))
    n += 1

print('피보나치 수열의 합은 {}입니다'.format(sumN))


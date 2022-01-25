# 계차수열

inputAN1 = int(input('a1 입력 : '))
inputAn = int(input('an의 알고싶은 n번째항 입력 : '))
inputBN1 = int(input('b1 입력 : '))
inputBd = int(input('수열 bn의 공차 입력 : '))

sumBn = 0
for i in range(1, (inputAn+1) ):
    valueAn = inputAN1 +sumBn
    sumBn = (i*(inputBN1 + inputBN1 + ((i-1)*inputBd))) // 2
    print('an의 {}번째 항은 {}입니다'.format(i,valueAn))





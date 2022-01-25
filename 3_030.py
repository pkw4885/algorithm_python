# 카드에서 원하는 조합이 나올 확률 구하기

numN = int(input('총 종이의 장 수 : '))
numR = int(input('뽑을 종이의 장 수 : '))
numNone = int(input('꽝의 장 수 : '))
print('선물 종이의 개수는 {} 장'.format(numN-numNone))
numPre = numN-numNone
numNoneCatch = int(input('꽝은 몇 장 뽑고 싶음?'))
print('뽑을 선물 종이의 개수는 {} 장'.format(numR - numNoneCatch))

numPreCatch = numR - numNoneCatch

if numR > numN:
    print('뽑는 종이의 총 개수를 잘못 입력했습니다')


if numNoneCatch > numNone:
    print('뽑는 꽝의 개수를 잘못 입력했습니다')


if numPreCatch > numPre:
    print('뽑는 선물의 개수를 잘못 입력했습니다')

def proFun(n,r):

    resultP = 1
    resultR = 1

    for i in range(n, (n - r), -1):
        resultP *= i

    for i in range(1, (r + 1)):
        resultR *= i

    return resultP//resultR

print( '{} %'.format(100*int(proFun(numNone,numNoneCatch))*int(proFun(numPre,numPreCatch))/(int(proFun(numN,numR)))))




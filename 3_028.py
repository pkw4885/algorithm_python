numN = int(input('numN 입력 : '))
numR = int(input('numR 입력 : '))
resultP = 1
resultR = 1
resultC = 1

for n in range(numN, (numN - numR), -1):
    resultP *= n

for n in range(1, (numR+1)):
    resultR *= n

print('P값 : {}, r!값 : {}, C값 : {}'.format(resultP, resultR, (resultP//resultR)))

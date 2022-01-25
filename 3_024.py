# 군수열

inputN = int(input('n항 입력 : '))

flag = True

n=1
nCnt = 1
while flag:

    for i in range(1, (n+1)):
        print('{} '.format(i), end='')
        nCnt += 1

        if (nCnt > inputN):
            searchN = i
            flag = False
            break

    print()
    n += 1

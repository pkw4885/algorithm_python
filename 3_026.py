#순열 8P3

# numN = int(input('numN 입력 : '))
# numR = int(input('numR 입력 : '))
# result = 1
#
# for n in range(numN, (numN - numR), -1):
#     print('n : {}'.format(n))
#     result = result*n
#
# print('result : {}'.format(result))

#원순열 - 원탁

n = int(input('원탁에 앉는 친구 수 입력 : '))
result = 1
for i in range(1, n):
    result *= i

print('result : {}'.format(result))

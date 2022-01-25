#팩토리얼

inputN = int(input('n입력 : '))

# result = 0
# for n in range(1, (inputN+1)):
#     result *= n
# print('{} 팩토리얼은 {}이다'.format(inputN, result))

def factorial(n):
    if n == 1: return 1
    return n * factorial(n-1)
print('{} 팩토리얼은 {}이다'.format(inputN, factorial(inputN)))

import math
print('{} 팩토리얼은 {}이다'.format(inputN, math.factorial(inputN)))

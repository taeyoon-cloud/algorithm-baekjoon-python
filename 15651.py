# 15651번: N과 M(3)
from itertools import product
n, m = map(int, input().split())

# result = []

# def backTracking(num):
#     if num == m:
#         print(*result)
#         return
    
#     for i in range(1, n+1):
#         result.append(i)
#         backTracking(num+1)
#         result.pop()


# backTracking(0)


result = list(product(range(1, n+1), repeat = m))

for res in result:
    print(*res)



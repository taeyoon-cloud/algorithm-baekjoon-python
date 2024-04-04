# 15652번: N과 M(4)

n, m = map(int, input().split())
result = []


# def backTracking(num):
#     if num == m:
#         print(*result)
#         return
    
#     for i in range(1, n+1):
#         if len(result) == 0:
#             result.append(i)
#             backTracking(num + 1)
#             result.pop()
#         if len(result) > 0 and result[-1] <= i:
#             result.append(i)
#             backTracking(num+1)
#             result.pop()


# backTracking(0)


def backTracking2(num):
    if len(result) == m:
        print(*result)
        return
    
    for i in range(num, n + 1):
        result.append(i)
        backTracking2(i)
        result.pop()

        

backTracking2(1)
# 15656번: N과 M(7)

n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
result = []

def backTracking(num):
    if num == m:
        print(*result)
        return
    
    for i in range(n):
        result.append(arr[i])
        backTracking(num+1)
        result.pop()


backTracking(0)
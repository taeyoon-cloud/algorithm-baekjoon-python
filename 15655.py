# 15655번: N과 M(6)

n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
result = []


def backTracking(num):
    if len(result) == m:
        print(*result)
        return
    
    for i in range(num, n):
        result.append(arr[i])
        backTracking(i+1)
        result.pop()


backTracking(0)
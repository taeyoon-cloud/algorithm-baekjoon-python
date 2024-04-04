# 15657번: N과 M(8)

n, m = map(int, input().split())
arr = list(map(int, input().split()))

result = []
arr.sort()

def backTracking(num):
    if len(result) == m:
        print(*result)
        return
    
    for i in range(num, n):
        result.append(arr[i])
        backTracking(i)
        result.pop()


backTracking(0)
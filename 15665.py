# 15665번: N과 M (11)

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

result = []

def backTracking():
    if len(result) == m:
        print(*result)
        return
    
    remember = 0
    for i in range(n):
        if arr[i] != remember:
            remember = arr[i]
            result.append(arr[i])
            backTracking()
            result.pop()

backTracking()
# 15666번: N과 M (12)

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

result = []

def backTracking(num):
    if len(result) == m:
        print(*result)
        return
    
    remember = 0
    for i in range(num, n):
        if arr[i] != remember:
            result.append(arr[i])
            remember = arr[i]
            backTracking(i)
            result.pop()


backTracking(0)

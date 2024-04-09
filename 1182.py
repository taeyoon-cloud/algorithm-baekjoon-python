# 1182번: 부분수열의 합

n, s = map(int, input().split())
arr = sorted(list(map(int, input().split())))

# 부분수열의 합이 S가 되는 경우의 수
answer = 0

result = []

def backTracking(num):
    if len(result) > 0 and sum(result) == s:
        global answer
        answer += 1
        # return
    
    for i in range(num, n):
        result.append(arr[i])
        backTracking(i+1)
        result.pop()


backTracking(0)
print(answer)
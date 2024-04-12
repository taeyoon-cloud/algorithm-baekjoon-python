# 6603번: 로또
import sys
input = sys.stdin.readline

def backTracking(num):
    if len(result) == 6:
        print(*result)
        return
    
    for i in range(num, cnt):
        result.append(arr[i])
        backTracking(i + 1)
        result.pop()

while True:
    line_input = list(map(int, input().split()))

    if line_input[0] == 0:
        break

    cnt = line_input[0]
    arr = line_input[1:]

    result = []

    backTracking(0)
    print()


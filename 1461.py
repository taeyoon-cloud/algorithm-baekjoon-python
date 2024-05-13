# 1461번: 도서관
# 음수와 양수를 나눠서 계산한다.
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

plus_arr = []
minus_arr = []

for num in arr:
    if num > 0:
        plus_arr.append(num)
    else:
        minus_arr.append(-num) # 양수로 입력

plus_arr.sort(reverse=True) # 내림차순 정렬
minus_arr.sort(reverse=True) # 내림차순 정렬

total = 0 # 걷는 걸음 수의 총합

# 일단 m씩 건너 뛴 값의 2배를 추가
for i in range(0, len(plus_arr), m):
    total += plus_arr[i] * 2

# 일단 m씩 건너 뛴 값의 2배를 추가
for i in range(0, len(minus_arr), m):
    total += minus_arr[i] * 2

# 양수가 없다면, 음수에서 가장 절댓값을 마지막으로 도착한다.
# 그리고 다시 돌아오는 걸음이 필요 없으므로 빼준다.
if not plus_arr:
    total -= minus_arr[0]

# 음수가 없을 때도 동일하게 처리해준다.
elif not minus_arr:
    total -= plus_arr[0]
# 둘 다 있다면, 음수, 양수 중 절댓값이 가장 큰 값을 마지막을 도착한다.
# 해당 칸에서 다시 돌아오는 걸음이 필요 없으므로 빼준다.
else:
    total -= max(minus_arr[0], plus_arr[0])

print(total)





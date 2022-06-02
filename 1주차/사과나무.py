n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

result = 0
start = n//2
end = n//2

for i in range(n):
    for j in range(start, end + 1):
        result += arr[i][j]
        if i < n // 2:
            start -= 1
            end += 1
        else:
            start += 1
            end -= 1
print(result)
# 다이아몬드 모양 면적을 구하는 것으로, n//2번째 행을 기준으로
# start 인덱스와 end 인덱스를 점차 늘리고, 좁히게 해서 구한다.
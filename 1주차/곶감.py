n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

m = int(input())

for i in range(m):
    row, direction, k = map(int,input().split())
    # 왼쪽방향으로 이동
    if direction == 0:
        for _ in range(k):
            temp = arr[row-1].pop(0)
            arr[row-1].append(temp)
    # 오른쪽 방향으로 이동
    else:
        for _ in range(k):
            temp = arr[row-1].pop()
            arr[row-1].insert(0,temp)

# 모래시계 모양의 면적 구하기
start = 0
end = n - 1
result = 0
for i in range(n):
    for j in range(start,end+1):
        result += arr[i][j]
    if i < n // 2:
        start += 1
        end -= 1
    else:
        start -= 1
        end += 1
print(result)
# 왼쪽 또는 오른쪽으로 배열의 원소들을 이동시킬 때, pop 과 insert를 반복해서 구할 수 있다. 한 칸씩 이동!
# start, end 인덱스 변수를 사용할 때 for문에 적용시, end 까지 반복해야하므로 +1 해주는 것 명심.

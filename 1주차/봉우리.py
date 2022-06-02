n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
# 맨위, 맨아래, 각 행의 앞과 뒤에 0을 추가 for 중복문을 이용하지 않고도 간단히 구현.
arr.insert(0,[0]*n)
arr.append([0]*n)

for i in range(n):
    arr[i].insert(0,0)
    arr[i].append(0)

count = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        if all(arr[i][j] > arr[i+dx[k]][j+dy[k]] for k in range(4)):
            count += 1
print(count)
# all 함수는 모든 조건을 검사하는 함수. 즉 상하좌우로 해당 수가 제일 크다면 True 반환.
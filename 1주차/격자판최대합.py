n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]
largest = -2147000000
# 행과 열의 합 구하기
for i in range(n):
    rowSum = 0
    colSum = 0
    for j in range(n):
        rowSum += arr[i][j]
        colSum += arr[j][i]
    if largest < rowSum:
        largest = rowSum
    if largest < colSum:
        largest = colSum
# 두 대각선의 합 구하기
crossSum1 = 0
crossSum2 = 0
for i in range(n):
    crossSum1 += arr[i][i]
    crossSum2 += arr[i][n-i-1]

if largest < crossSum1:
    largest = crossSum1
if largest < crossSum2:
    largest = crossSum2

print(largest)

# 2차원 배열 생성시 arr = [list(map(int,input().split())) for _ in range(n)] 도 가능.
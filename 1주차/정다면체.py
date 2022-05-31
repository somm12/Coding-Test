n, m = map(int,input().split())
arr = [0] * (n+m+1)

for i in range(1,n+1):
    for j in range(1,m+1):
        arr[i+j] += 1

maxPercent = max(arr)

for i in range(n+m+1):
    if arr[i] == maxPercent:
        print(i,end=' ')
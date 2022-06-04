n = int(input())

arr = list(map(int,input().split()))
originalArr = [0] * n

for i in range(n):
    count = 0
    for k in range(n):
        if originalArr[k] == 0:
            count += 1
        if count > arr[i]:
            originalArr[k] = i + 1
            break

for value in originalArr:
    print(value, end=' ')
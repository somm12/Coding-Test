# 소수의 개수

n = int(input())
check = [0] * (n+1)
count = 0

for i in range(2,n+1):
    if check[i] == 0:
        count += 1
        for j in range(i,n+1,i):
            check[j] = 1
print(count)
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

# 처음 2를 소수라고 체크하고 그 뒤 2의 배수, 3의 배수,, 등 배수를 미리 체크해서 제외시키는 방식 
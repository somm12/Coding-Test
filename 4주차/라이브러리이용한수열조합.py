import itertools as it

n, k = map(int,input().split())

a = list(map(int,input().split()))
m = int(input())
cnt = 0
 
for x in it.combinations(a, k):
    if sum(x) % m == 0:
        cnt += 1
print(cnt)

# 주의해야할 것은 항상 라이브러리에 너무 의존하지 않는 것!!
import itertools as it

n, f = map(int,input().split())
b = [1] * n
cnt = 0

for i in range(1,n):
    b[i] = b[i-1] * (n - i)//i

a = list(range(1, n + 1))
for tmp in it.permutations(a):
    sum = 0
    for L, x in enumerate(tmp):
        sum += (x * b[L])
    if sum == f:
        for x in tmp:
            print(x, end=' ')
        break

# 파스칼 삼각형의 합으로 수열 추측하기 문제이다. 전과 다르게, 라이브러리를 이용해서 풀면 위와 같다.
# 파이썬은 수열을 자동으로 만들어주는 라이브러리를 제공해 주는데, 라이브러리에 너무 의존하면 안된다!!
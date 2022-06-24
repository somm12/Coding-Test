n, m = map(int,input().split())
g = [ [0] * (n + 1) for _ in range(n+1)]

for _ in range(m):
    a, b, d = map(int,input().split())
    g[a][b] = d
for i in range(1,n+1):
    for j in range(1,n+1):
        print(g[i][j], end=' ')
    print()

# 가중치가 있는 그래프를 인접행렬로 표현하려면, 입력이 a 에서 b 연결의 가중치가 d 이기 때문에
# g[a][b] = d 라고 표현할 수 있다.

# 기억하면 좋은 것: 2차원 배열 표현시 [[0] * (열개수) for _ in range(행개수)]로 간단히 표현 가능.

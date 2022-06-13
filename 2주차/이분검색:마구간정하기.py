def Count(len):
    cnt = 1
    ep = Line[0]
    for i in range(1,n):
        if Line[i] - ep >= len:
            cnt += 1
            ep = Line[i]
    return cnt

n, c = map(int,input().split())
Line = []
for _ in range(n):
    Line.append(int(input()))

Line.sort()
lt = 1
rt = Line[-1]
while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) >= c:
        result = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(result)


# 이분검색 또는 결정알고리즘은 유형이 비슷하다. 문제에서 구하려하는 것의 범위를 찾고 
# 그 범위를 점점 좁혀나가면서 구하고자 하는 값을 찾는다.
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

# N개의 마구간에서 C마리의 말을 배치한다. N개의 마구간 좌표를 입력을 받고, 
# 말을 배치하는데, 가장 가까운 말 사이의 거리가 최대가 될 때 그 최대값을 구하자.

# 이분검색 또는 결정알고리즘은 유형이 비슷하다. 문제에서 구하려하는 것(말사이의 거리)의 범위를 찾고 
# 그 범위를 점점 좁혀나가면서 구하고자 하는 값을 찾는다.
# 최대가 되는 거리: 최소 말이 2마리는 입력이 되므로 정렬한 좌표 배열의 첫원소와 마지막원소의 차이가 최대거리다.

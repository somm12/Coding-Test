k, n = map(int,input().split())
line = []
largest = 0

for i in range(k):
    tmp = int(input())
    line.append(tmp)
    largest = max(largest,tmp)

lt = 1
rt = largest
result = 0
def Count(len):
    count = 0 
    for x in line:
        count += x // len
    return count
while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) >= n:
        lt = mid + 1
        result = mid
    else:
        rt = mid - 1

print(result)

# 이분탐색을 이용해서 랜선을 자르자.
# K개의 랜선을 잘라서 N개 이상으로 만들고 그 자른 N의 길이의 최대를 구하자.
# 입력 받은 K개의 수 중에서 가장 큰 수 largest를 찾고 1 ~ largest까지 자른 랜선의 길이 범위를 둔다.
# 두 범위 사이의 mid를 구하고 각 k개의 랜선으로 나누어 개수가 n개 이상을 만족한다면 일단 값 저장
# 하지만 더 길이를 최대로 만들 수 있기 때문에 길이를 늘려 나가기 위해 lt = mid + 1
# 반대로 n개에 도달 못했다면 길이를 줄이기 위해서 rt = mid - 1로 줄인다.
# 반복하다가 lt > rt 되면 반복 종료.
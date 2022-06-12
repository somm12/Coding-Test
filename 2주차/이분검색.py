n, m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

lt = 0
rt = n - 1

while lt <= rt:
    mid = (lt + rt) // 2
    if arr[mid] == m:
        print(m + 1)
        break
    elif arr[mid] < m:
        lt = mid + 1
    else:
        rt = mid - 1

# 전제조건 : 이분탐색 O(logN) 을 위해서는 오름차순 또는 내림차순으로 정렬이 되어있어야함.
# 참고로 파이썬 내장함수 sort()는 nlogn 시간복잡도를 가지고 있다. 밑은 2임.

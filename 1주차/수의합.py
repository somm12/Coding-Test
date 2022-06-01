n, m = map(int,input().split())

arr = list(map(int,input().split()))
# left 인덱스 부터 right 인덱스 전! 까지의 합이 m과 같은 경우를 구한다.
left = 0
right = 1
total = arr[0]
count = 0

while True:
    if total < m:
        if right < n:
            total += arr[right]
            right += 1
        else:
            break
    elif total == m:
        count += 1
        total -= arr[left]
        left += 1
    else:
        total -= arr[left]
        left += 1
print(count)

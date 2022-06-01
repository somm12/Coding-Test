n, m = map(int,input().split())

arr = list(map(int,input().split()))

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

# left 인덱스 부터 right 인덱스 전! 까지의 합이 m과 같은 경우를 구한다.
# 만일 합이 m과 같거나 m보다 커진다면 left를 한 칸 옮겨야 하므로 전까지 더했던 total에서 arr[left]를 빼줘야한다.
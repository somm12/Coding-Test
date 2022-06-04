
n = int(input())
arr = map(int,input().split())

left = 0
right = n - 1
# 마지막에 저장될 수를 담는 변수
last = 0
# 왼쪽 또는 오른쪽 중 어느 쪽에서 가져왔는지 기록할 result
result = ""
# 가장 왼쪽 / 오른쪽 중 두 가지 값을 튜플 형태로 담기위한 배열
temp = []

while left <= right:
    if arr[last] < arr[left]:
        temp.append((arr[left],"L"))
    if arr[last] < arr[right]:
        temp.append((arr[right],"R"))
    temp.sort()
    if len(temp) == 0:
        break
    else:
        result += temp[0][1]
        last = temp[0][0]
        if temp[0][1] == "L":
            left += 1
        else:
            right += 1
    temp.clear()
print(len(result))
print(result)

# 입력 받은 수열을 가장 왼쪽 이나 오른쪽에서 하나씩 꺼내어 증가수열을 만드는데, 길이가 최대가 되게끔한다.
# 어느 쪽에서 가져왔는지 기록해서 LRLLL 와 같은 문자열을 출력, 그리고 최대 수열 길이 출력
# 왼쪽와 오른쪽을 대변할 변수 인덱스 left right를 이용해서 가장 최근에 저장된 수보다 큰지 확인
# 그리고 두 군데 모두 클 때 대비해서 증가수열을 만들어야하니 sort사용
# 튜플을 이용해서 (숫자,"L"/"R") 한 번에 꺼낸 방향기록 과 수열 길이를 구한다.
# 왼쪽 오른쪽 둘 중 하나씩 꺼내는 반복을 하기 때문에 한 단계를 확인하면 다시 clear로 temp 배열 비움. => 만일 두 양쪽 모두 last 보다 작을 경우 수열을 더이상 못만듦.

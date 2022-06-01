n = int(input())
arr1 = list(map(int,input().split()))

m = int(input())
arr2 = list(map(int,input().split()))
# 두 배열의 인덱스를 가리키는 포인터 역할 p1,p2
p1 =0 
p2 = 0
newArr = []

while p1 < n and p2 < m:
    if arr1[p1] <= arr2[p2]:
        newArr.append(arr1[p1])
        p1 += 1
    else:
        newArr.append(arr2[p2])
        p2 += 1

if p1 < n:
    newArr += arr1[p1:]
else:
    newArr += arr2[p2:]

print(newArr)

# 이미 정려된 두 리스트를 입력, 두 리스트를 오름차순으로 정렬된 리스트를 반환.
# 두 리스트가 이미 정렬되어 있기 때문에 sort함수(nlogn 복잡도)를 사용하지 않고 n 번만 연산할 수 있도록 할 수 있다.
n = int(input())
body = []
for i in range(n):
    h, w = map(int,input().split())
    body.append((h,w))

body.sort(reverse=True)

count = 0
largest = 0

for h, w in body:
    if largest < w:
        count += 1
        largest = w

print(count)

# 씨름 선수의 키와 몸무게가 다른 어떤 선수와도 둘 다 작으면 뽑히지 않는다.
# for 중복문을 이용해서 일일이 확인할 수 있지만, 효율적이지 않다.
# sort를 키 중심 내림차순을 한 뒤, 몸무게만 앞의 선수와 비교해 더 큰지 비교. => 시간 복잡도가 줄어듦.
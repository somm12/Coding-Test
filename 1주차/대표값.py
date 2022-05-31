n = int(input())
arr = list(map(int,input().split()))
# round 사용시 조심: round(4.5) => 4 출력 됨.
average = (sum(arr)/n) + 0.5
average = int(average)
min = 21470000

#enumerate : 배열의 index와 값을 받아오는 내장함수.

for idex, value in enumerate(arr):
    temp = abs(average - value)
    if temp < min:
        min = temp
        score = value
        number = idex+1
    elif temp == min:
        if value > score:
            score = value
            number = idex+1
#몇 번째 인지 알아야하는데, index를 사용했으니 idex + 1을 해야한다.
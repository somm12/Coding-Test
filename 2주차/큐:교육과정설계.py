from collections import deque
necessary = list(input())

n = int(input())


for i in range(n):
    newQ = []
    lectures = deque(list(input()))
    for value in lectures:
        if value in necessary:
            newQ.append(value)
    
    if necessary == newQ:
        print("#%d YES" % (i + 1))
    else:
        print("#%d NO" % (i + 1))
# 나의 풀이
# 필수과목은 A,B,C,D,, 등으로 교육과정을 설계하는데, 입력받은 필수과목은 꼭 순서대로 이수해야한다.
# 순서대로 이수했는지 확인해야하므로 입력받은 설계를 하나씩 필수과목에 해당하면 빈 리스트에 옮긴다.
# 반복문이 끝나면 옮겨진 새로운 리스트 newQ에는 초기 순서가 유지된 채로 필수과목이 남아있다. 
# newQ 와 lectures와 같은지 확인함으로써 순서가 같은지 알아낸다.


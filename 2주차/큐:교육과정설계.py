from collections import deque
necessary = list(input())

n = int(input())


for i in range(n):
    newQ = []
    lecturesPlan = deque(list(input()))
    for value in lecturesPlan:
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

need = input()
n = int(input())

for i in range(n):
    plan = input()
    dq = deque(need)
    # 순서만 맞는지 확인
    for x in plan:
        if x in dq:
            if x != dq.popleft():
                print("#%d NO" % (i + 1))
                break
    # 필수과목을 넣었는지 확인
    else:
        if len(dq) == 0:
            print("#%d YES" % (i + 1))
        else:
            print("#%d NO" % (i + 1))

# 정답 풀이
# for 반복문으로 plan의 과목을 하나씩 확인. 그 과목이 need 필수과목에 해당하고, popleft한 것과
# 같다면, 즉 순서가 같다면 넘어가고 만약 같지 않다면 바로 no를 출력한다. 정상적으로 종료가 되면(else문) 일단
# 순서가 다른 경우는 아닌 것.
# 하지만 필수과목을 넣지 않았을 수도 있기 때문에 for문이 정상종료 되고난 후, dq의 길이가 0인지 확인.

# 생각: 배열은 하나 더 사용했는지만 개인적으로 내 풀이가 더 쉽게 떠오를 수 있는 방법인 것 같다.
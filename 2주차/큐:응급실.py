from collections import deque
n, m = map(int,input().split())

patientDanger = deque(list(map(int,input().split())))
count = 0

while True:
    largest = patientDanger[0]
    for i in range(1,n):
        if patientDanger[i] > largest:
            patientDanger.append(patientDanger.popleft())
            m -= 1
            break
    else:
        if m == 0:
            count += 1
            break
        else:
            count += 1
            patientDanger.popleft()
            patientDanger.append(0)
            m -= 1
    if m == -1:
        m = len(patientDanger) - 1

print(count)

# 나의 풀이
# 응급실 환자 m 번째 환자는 몇 번째에 진료를 받을 수 있는지 구한다.
# 순서대로 환자를 진료하지만 해당 환자보다 대기목록에 있는 환자의 위험도가 더 크다면 다시 맨 뒤로 보낸다.

# 큐를 이용해서 첫번째 원소보다 큰 원소가 하나라도 있으면 바로 다시 popleft와 append를 한다.
# for문을 통한 비교문이 정상적으로 종료가 되면(첫번째 원소가 가장 클 경우) 진료를 받을 수 있게되어 count += 1
# m 번째 환자의 index와 m은 같다. 환자가 진료받을 시점 즉 m 이 0이 되는 시점에 for문이 정상적으로 종료되면
# 그 때 마지막으로 count += 1 한 뒤, count를 알아내면 된다.

# for문을 사용하고 pop을 계속하기 때문에 후에 index out of range오류가 나올 수 있으니
# popleft를 한 뒤, 배열의 길이를 유지하기 위해 0을 append했다.


n, m = map(int,input().split())
danger = [(pos,val) for pos, val in enumerate(list(map(int,input().split())))]
danger = deque(danger)
cnt = 0

while True:
    curent = danger.popleft()
    if any(curent[1] < x[1] for x in danger):
        danger.append(curent)
    else:
        cnt += 1
        if curent[0] == m:
            print(cnt)
            break

# 정답 풀이 - 더 쉽게 풀기.
# 문제를 풀려면 처음에 입력 받은 배열의 초기 index값이 필요하므로, 저장을 해놓으면 편하다.
# 예를 들어 튜플을 이용해서 index값을 저장해 놓는 것이다.

### 알게 된 것
# any 함수: 괄호안에 하나라도 만족하는지 체크해줌.
# enumerate 재등장 : 리스트의 인덱스와 값이 둘 다 필요할 때 유용한 함수.

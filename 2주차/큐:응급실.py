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

# 정답 풀이


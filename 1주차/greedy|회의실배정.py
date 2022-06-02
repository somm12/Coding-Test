n = int(input())
meeting = []
for _ in range(n):
    s, e = map(int,input().split())
    meeting.append((s,e))

meeting.sort(key=lambda x : (x[1],x[0]))

endTime = 0
count = 0
for start , end in meeting:
    if endTime <= start:
        count += 1
        endTime = end
    
print(count)
# for 문에서 변수 두 개 start, end 를 이용해서 각 배열의 회의시작, 끝나는 시간을 배정.
# sort를 하는 기준은 lambda 함수를 이용해서 바꿀 수 있다.
# lambda x : x[1] 으로 하지 않는 이유는 3 3 / 1 3 / 2 3  이 케이스에서 틀리게 된다.
# 답은 2개 지만, 1이 출력됨. 끝나는 시간이 같을 때, 시작 시간이 빠른 부분이 먼저 sort되어야 함!
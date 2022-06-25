def DFS(L,sum):
    global res
    if L > n:
        if res < sum:
            res = sum
    else:
        DFS(L + Ti[L], sum + Pi[L])
        DFS(L+1,sum)

if __name__ == "__main__":
    res = 0
    n = int(input())
    Ti = [0]
    Pi = [0]
    for _ in range(n):
        t, p = map(int,input().split())
        Ti.append(t)
        Pi.append(p)
    DFS(1,0)
    print(res)

# 최대 점수구하기 문제처럼, 어떤날에 상담을 하느냐 안하느냐가 포인트이다. 만약 1일째 상담을 하면 5일째부터
# 상담을 할 수 있고 만약 5일째 상담을 안한다면 6일째 상담으로 넘어가는 것이다. 역시 이 문제도 부분집합 문제를
# 활용해서 문제를 풀 수 있다. 대신 상담을 하면
# 현재 상담일(레벨) + 상담기간 => L +Ti[L] 로 업데이트 된다.
# 상담하지 않을 시, 다음으로 넘어가니 L+1로 재귀호출.
# 매개변수 L을 상담일자 기간의 합으로 두어서 sum도 sum + Pi[L]로 업데이트를 한다.

# 지금까지 배웠던 것을 회상하면서, 어떤 식으로 문제를 풀 수 있을지 그림을 그린다.
# 그대로 코드로 정확하게 쓴다.
# 에디터에 옮겨쓰고 테스트 해보자.
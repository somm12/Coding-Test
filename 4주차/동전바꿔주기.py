def DFS(L,sum):
    global cnt
    if sum > T:
        return
    if L == k:
        if sum == T:
            cnt += 1
    else:
        for i in range(cn[L] + 1):
            DFS(L+1, sum + (cv[L] * i))
    
if __name__ == "__main__":
    T = int(input())
    k = int(input())
    cv = list()
    cn = list()
    for i in range(k):
        a, b = map(int,input().split())
        cv.append(a)
        cn.append(b)
    cnt = 0
    DFS(0,0)
    print(cnt)

# T 원을 거스름 돈으로 주려고 한다. 동전 종류가 k개이고, 각 동전 금액 cv 와 각 동전 개수 cn 배열에 입력을
# 받고 T원을 줄 수 있는 모든 경우의 수를 구하자

# 거스름 돈을 만들 때, 5원 10원 1원 이 세개 종류가 있고 각각 3개, 2개, 5개 가 있다고 하자
# 그러면 5원은 0원 ~ 3개까지 사용가능하고, 10원도 0원에서 2개까지, 1원은 0개에서 5개 까지 쓸 수 있고
# 이 개수를 몇 개 쓸 지 골라내어 20원이 되게 만들면 되는 것이다.

# 트리는 0원 부터 시작해서 첫 레벨은 5원부터 0개 ~ 3개사용했을 때 금액으로 더하며 가지를 뻗어나간다.
# 그 다음 레벨은 다시 10원을 0개 ~ 2개 사용했을 때 뻗어나가고 .. 반복.
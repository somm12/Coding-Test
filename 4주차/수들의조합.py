def DFS(L,s):
    global cnt, res
    if L == k:
        if sum(res) % m == 0:
            cnt += 1
    else:
        for i in range(s, n):
            res[L] = arr[i]
            DFS(L+1,i+1)

if __name__ == "__main__":
    n, k = map(int,input().split())
    arr = list(map(int,input().split()))
    m = int(input())
    res = [0] * k
    cnt = 0
    DFS(0,0)
    print(cnt)

# n개의 수에서 k개를 뽑았을 때 그 합이 m의 배수인 경우의 개수를 구하자.
# 나의 풀이: 조합구하기에서 해당 조합의 sum이 sum % m == 0 가 되는지 확인만 하면 된다.
# 따라서 조합을 답은 배열 res의 sum을 가지고 확인했다.

def DFS(L,s,sum):
    global cnt, res
    if L == k:
        if sum % m == 0:
            cnt += 1
    else:
        for i in range(s, n):
            DFS(L+1,i+1,sum + arr[i])

if __name__ == "__main__":
    n, k = map(int,input().split())
    arr = list(map(int,input().split()))
    m = int(input())
    res = [0] * k
    cnt = 0
    DFS(0,0,0)
    print(cnt)
# 정답풀이: 조합을 구해서 출력할 필요는 없고 그 합 sum을 구하는 것이 목적이기 때문에 매개변수로 전달하여
# 하나씩 arr[i] 이 더해지도록 하는 방법을 사용한다. 따라서 조합을 담을 배열이 필요없어진다.

# 해당 조합 형태가 필요 없으면 굳이 배열을 선언하지 말자!!!! 매개변수 하나로 문제 해결이 가능할 수 있다.
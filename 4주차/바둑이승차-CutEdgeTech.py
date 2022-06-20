
def DFS(index, sum):
    global max
    if sum > C:
        return
    if index == N:
        if sum > max:
            max = sum
    else:
        DFS(index + 1, sum + arr[index])
        DFS(index + 1, sum)

if __name__ == "__main__":
    C, N = map(int,input().split())
    arr = []
    max = 0
    for _ in range(N):
        arr.append(int(input()))

    DFS(0,0)
    print(max)
# 나의 풀이
# 바둑이들을 무게 C가 넘지 않게 최대한 무겁게 트럭에 싣자.
# DFS를 이용해서 매개변수를 sum으로 전달해서 C를 넘으면 return, max를 전역변수로 두어서 sum이 max보다 크면
# max를 update한다.

def dfs(index, sum, tsum):
    global max
    if sum + (total - tsum) < max:
        return
    if sum > C:
        return
    if index == N:
        if sum > max:
            max = sum
    else:
        DFS(index + 1, sum + arr[index],tsum + arr[index])
        DFS(index + 1, sum,tsum + arr[index] )

if __name__ == "__main__":
    C, N = map(int,input().split())
    arr = []
    max = 0
    for _ in range(N):
        arr.append(int(input()))
    total = sum(arr)
    DFS(0,0)
    print(max)

# 정답풀이 하지만 내 풀이대로 제출을 하면 시간초과가 발생한다. 그래서 cut 조건이 하나 더 필요하다.
# 현재 sum값이 최대값일 수 있다!는 생각을 할 수 있어야한다.
# 만약 (현재까지 만든 부분집합의 합: sum + 앞으로 남은 모든 숫자들 total-tsum) 이 둘의 합이 
# 현재 max 보다 작으면 끝까지 재귀를 하면서 답을 구할 필요가 없다. 
# tsum은 원소를 포함 o,x 상관없이, 지금까지 지나쳐 왔던 모든 숫자들의 합. total - tsum: 앞으로 남은 숫자들의 모든 합.
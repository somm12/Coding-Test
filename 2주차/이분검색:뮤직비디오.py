from xmlrpc.server import DocXMLRPCRequestHandler


n, m = map(int,input().split())

songLen = list(map(int,input().split()))
songLen.sort()

# lt와 rt 는 DVD가 수용할 수 있는 용량 범위
lt = 1
rt = sum(songLen) 
result = 0
def Count(capacity):
    cnt = 1
    sum = 0
    for x in songLen:
        if sum + x > capacity:
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt
result = 21470000
maxx = max(songLen)
while lt <= rt:
    mid = (lt  + rt) // 2
 
    if maxx <= mid and Count(mid) <= 3:
        result = min(result,mid)
        rt = mid - 1
    else:
        lt = mid + 1

print(result)

# N개의 곡을 M개의 DVD에 수록하려한다. 반드시 1번, 5번 곡이 수록된다면 1 ~ 5 까지 모두 곡을 수록해야한다. 연속적으로.
# 곡들을 수용할 수 있는 DVD 용량의 최소를 구하시오.
# 조심해야할 것 DVD용량을 30으로 했는데 DVD개수가 2개로 나왔다면 답이 되지 않는게 아니다.
# M개의 DVD로 만들기로 했다고 했으니, 2개가 나와도 충분히 역량내 범위이므로 답이 될 수 있다는 것!!!!!

# Count함수를 구현할 때, 일단 더해보고, 수용제한량이 넘어서면 그 수를 다시 sum에 할당하면 그 다음수터 바로
# 합을 구할 수 있게된다.
# *** 최소한 길이가 가장 큰 곡의 길이가 DVD 용량이상이어야함!!!
card = [i for i in range(21)]
print(card)
card = list(range(21))
print(card)
for _ in range(10):
    start, end = map(int,input().split())
    for i in range((end-start+1)//2):
        card[start+i], card[end-i] = card[end-i], card[start+i]
# 0은 출력되면 안됨. 
card.pop(0)
for i in card:
    print(i,end=' ')
# 배열 초기화 할 때, card = list(range(21)) 과 같은 방식으로도 가능.
# for i in range 사용할 때 , i 를 쓸 필요가 없다면 _ 로 사용가능. 변수에 수를 대입하는 것도 시간이 걸리기에
# 계산 시간을 줄이는 데 조금이라도 보탠다.
# 파이썬에서는 swap를 a, b = b, a 방식으로 가능.
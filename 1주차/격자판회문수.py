board = [list(map(int,input().split())) for _ in range(7)]

count = 0
for i in range(7):
    for j in range(3):
        temp = board[i][j:j+5]
        if temp == temp[::-1]:
            count += 1
        
        for k in range(2):
            if board[i+4-k][j] != board[k][j]:
                break
        else:
            count += 1

print(count)
#회문수인지 확인할 때 해당 문자열 또는 배열의 길이//2 만큼만 비교해도 된다. 중간 인덱스를 향해서 양쪽에서 
#차근차근 비교하는 방법이다.
#참고로 파이썬 배열 파씽은 2차원 배열에서는 arr[i][j:j+xx] 즉 열을 통해서만 사용가능하다.
# arr[i:i+k][j] 이와 같이 행을 통한 파씽은 사용할 수 없고 그래서 반복문을 사용한다.
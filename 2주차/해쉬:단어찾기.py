n = int(input())
wordsInNote = []
wordsInPoetry = []
for i in range(n):
    wordsInNote.append(input())

for i in range(n-1):
    value = input()
    wordsInPoetry.append(value)
    if value in wordsInNote:
        wordsInNote.pop(wordsInNote.index(value))
print(wordsInNote[0])

# 해쉬는 Key에 Value(데이터)를 저장하는 자료구조
# 파이썬에서는 dictionary 사용하면 된다. key값과 value 값을 자주 사용한다면 해쉬를 선택해도 좋을 것 같다.
# a = {'a':1, 'b':2} 처럼 정의할 수 있음 a[Key] 와 같이 value 값에 접근 가능

# a.keys() : key 값 배열 반환
# a.values() : value 값을 모은 배열 반환
# a.items() : key , value 쌍을 튜플로 묶어 배열로 반환 ex)[('name', 'pey'), ('phone', '0119993323'), ('birth', '1118')]
# a.clear() : key,value 쌍 모두 지우기

# 나의 풀이
# 두 배열에 각각 시에 쓰인 단어와 쓰일 단어를 초기화하고 for문 반복을 통해 wordsInPoem이 wordsInNote에
# 존재한다면, wordsInNote에서 해당 단어의 index를 찾아서 pop한다. 마지막으로 담은 단어가 답이된다.


n = int(input())
poem = dict()

for i in range(n):
    word = input()
    poem[word] = 1

for _ in range(n-1):
    word = input()
    poem[word] = 0

for key,val in poem.items():
    if val == 1:
        print(key)
        break 
 
# 정답풀이
# 시에 사용되지 않은 단어를 찾기 위해서 key에는 단어를, value에는 숫자 1을 통해서 초기화한 후,
# 시에 사용된 단어가 입력되면 해당 key 값의 value를 0으로 할당.
# for 반복문을 items() 딕셔너리 기능을 적용해서 key 값과 value를 동시에 활용하여 value가 1인 key 출력

# 문제풀이 후 든 생각
# 이처럼 index 값과 value 즉 데이터 값 모두가 필요할 경우에는 딕셔너리를 써도 괜찮았을 것이다.
# for 반복문 사용은 좋지만 혹시 하나의 답을 바로 찾고 그 후의 반복은 필요하지 않다면 바로 break문을 사용
# 하자. 불필요한 반복을 줄여서 연산시간을 줄일 수 있다.
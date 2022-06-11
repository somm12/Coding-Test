from typing import Dict


str1 = input()
str2 = input()

dicStr1 = dict()
dicStr2 = dict()

for word in str1:
    if word in dicStr1:
        dicStr1[word] += 1
    else:
        dicStr1[word] = 1
for word in str2:
    if word in dicStr2:
        dicStr2[word] += 1
    else:
        dicStr2[word] = 1

for key,value in dicStr1.items():
    if dicStr1[key] != dicStr2[key]:
        print("NO")
        break
else:
    print("YES")

# 나의 풀이
# 아나그램은 두 단어의 알파벳 구성이 같은 것을 아나그램이라고 한다. ex) AbaAeCe 와 baeeACA
# 입력받은 두 단어가 아나그램인지 판단하자.
# 먼저 입력받은 두 문자열을 for문 반복을 통해서 문자하나씩 확인을 하여
# 새로운 딕셔너리에 알파벳 구성이 어떻게 되는지 할당한다. -> 이미 딕셔너리에 있다면 +1 씩 아니라면 1을 할당하여
# 어떤 알파벳이 몇 개로 구성되어있는지 딕셔너리를 만든다.
# 두번째 문자열도 같은 방법으로 딕셔너리를 생성한뒤. items() 함수를 이용해서 두 키값의 value 즉 개수가 같은지
# 확인한다. 만약 for문이 정상적으로 종료 => else문을 이용해서 YES 를 출력.

for word in str1:
    dicStr1[word] = dicStr1.get(word,0) + 1
    
for word in str2:
    dicStr2[word] = dicStr2.get(word,0) + 1

for i in dicStr1.keys():
    if i in dicStr2:
        if dicStr1[i] != dicStr2[i]:
            print("NO")
            break
    else:
        print("NO")
else:
    print("YES")

# 정답 풀이
# 위와 같이 딕셔너리 함수 get을 사용하면 해당 key값이 존재하지 않으면 0을 반환 아니면 해당 key의 value이
# 반환된다. 이를 이용해서 한 줄짜리 코드로 줄일 수 있다는 장점이 있다.

# 여기서 내가 간과한 것!!!
# 내가 짠 코드는 키 값 구성만 확인한다, 그래서 YES인 경우에는 문제 없겠지만 아닌경우에는!
# 예를 들어 str1에 있는 알파벳이 str2에는 없다면?!! 아예 if문이 비교를 할 수 없어서 오류난다.
# 또한 굳이 구성이 일치하는지 확인할 때 key값만 있어도 되기 때문에 이 문제에서는 items 안써도 됨.

# 그래서 if 문을 통해서 if i in dicStr2 라고 확인을 한다. else과 쌍으로 만약 아니라면 NO!
# 만약 해당 알파벳이 있는데 개수가 달라도 NO! else문으로 정상종료가 됬다면 YES!
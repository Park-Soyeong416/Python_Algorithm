checkList = [0] * 4
myList = [0] * 4
checkSecret = 0

def myadd(c):
    global checkList, myList, checkSecret
    if c == 'A':
        myList[0] += 1
        if myList[0] == checkList[0]:
            checkSecret += 1
    elif c == 'C':
        myList[1] += 1
        if myList[1] == checkList[1]:
            checkSecret += 1
    elif c == 'G':
        myList[2] += 1
        if myList[2] == checkList[2]:
            checkSecret += 1
    elif c == 'T':
         myList[3] += 1
         if myList[3] == checkList[3]:
             checkSecret += 1

def myremove(c):
    global checkList, myList, checkSecret #전역변수를 함수 내에서 변경하고 싶을 때 global 사용
    if c == 'A':
        if myList[0] == checkList[0]:
            checkSecret -= 1
        myList[0] -= 1
    elif c == 'C':
        if myList[1] == checkList[1]:
            checkSecret -= 1
        myList[1] -= 1
    elif c == 'G':
        if myList[2] == checkList[2]:
            checkSecret -= 1
        myList[2] -= 1
    elif c == 'T':
        if myList[3] == checkList[3]:
            checkSecret -= 1
        myList[3] -= 1

S, P = map(int, input().split())
Result = 0
A = list(input())
checkList = list(map(int, input().split()))

for i in range(4):
    if checkList[i] == 0: #0이라는 건 이미 조건을 만족한다는 뜻
        checkSecret += 1

for i in range(P):
    myadd(A[i])

if checkSecret == 4:
    Result += 1

for i in range(P, S):
    j = i - P
    myadd(A[i])
    myremove(A[j])
    if checkSecret == 4:
        Result += 1

print(Result)
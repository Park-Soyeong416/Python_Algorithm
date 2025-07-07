N = int(input())
A = [0] * N

for i in range(N):
    A[i] = int(input())

stack = []
num = 1 #1부터 시작해서 오름차순으로 스택에 저장하고 출력할 것임
result = True #스택을 이용해 주어진 수열을 만들 수  있는 지 여부(True로 초기화 상태)
answer = [] # +, - 를 출력하기 위한 리스트

for i in range(N):
    su = A[i] #su는 입력된 수열(=만들어야 할 수열)의 순서를 가리킴
    if su >= num: #값이 같아질 때까지 append 수행
        while su >= num:
            stack.append(num)
            num += 1
            answer.append('+')
        stack.pop() #같아지는 순간 pop한다
        answer.append('-')
    else:
        n = stack.pop()
        if n > su: #스택의 가장 위의 수가 만들어야 할 수열의 수보다 크면 수열을 출력할 수 없음
            print("NO")
            result = False
            break
        else:
            answer.append('-')

if result:
    for i in answer:
        print(i)
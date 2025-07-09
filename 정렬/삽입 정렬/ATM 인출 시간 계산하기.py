N = int(input())
A = list(map(int, input().split()))
S = [0] * N

for i in range(1, N):
    insert_point = i
    insert_value = A[i] #삽입하고자 하는 값
    for j in range(i-1, -1, -1):
        if A[j] < A[i]: #자신보다 작은 값이 등장하면
            insert_point = j + 1 #그 작은 값 오른쪽이 내 자리
            break
        if j == 0: #작은 값이 등장하지 않은 채로 j가 0이 되었다면
            insert_point = 0 #내 자리는 가장 앞 자리
    for j in range(i, insert_point, -1):
        A[j] = A[j-1] #insert할 위치 파악했으니 나머지 부분 shift
    A[insert_point] = insert_value #insert

S[0] = A[0]

for i in range(1, N): #합 배열 생성
    S[i] = S[i-1] + A[i]

sum = 0

for i in range(0, N):
    sum += S[i]

print(sum)
import sys
input = sys.stdin.readline
print = sys.stdout.write

def merge_sort(s, e):
    if e-s < 1:
        return
    m = int(s + (e -s)/2) #절반으로 나눌 지점 구하기
    merge_sort(s, m) #앞 절반 합병 정렬
    merge_sort(m + 1, e) # 뒤 절반 합병 정렬
    for i in range(s, e + 1):
        tmp[i] = A[i]
    k = s
    index1 = s
    index2 = m + 1
    while index1 <= m and index2 <= e:
        if tmp[index1] > tmp[index2]: # 두 집단 중에서 작은 수가 해당하는 것을
            A[k] = tmp[index2] #대입시킨다
            k += 1
            index2 += 1
        else:
            A[k] = tmp[index1]
            k += 1
            index1 += 1
    while index1 <= m: # 한쪽 그룹이 모두 선택된 후 남아 있는 값 정리
        A[k] = tmp[index1]
        k += 1
        index1 += 1
    while index2 <= e: # 한쪽 그룹이 모두 선택된 후 남아 있는 값 정리
        A[k] = tmp[index2]
        k += 1
        index2 += 1

N = int(input())
A = [0] * int(N + 1)
tmp = [0] * int(N + 1)

for i in range(1, N + 1):
    A[i] = int(input())

merge_sort(1, N)

for i in range(1, N + 1):
    print(str(A[i]) + '\n')
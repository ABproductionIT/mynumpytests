
def solution(A):
    d = 1
    x = []
    if max(A) < 1:
        print(d)
    else:
        for i in range(len(A)-1):
            x.append(max(A) - A[i])
        if max(x) not in A:
            print(max(x))
        else:
            print(max(A)+1)


solution(A)

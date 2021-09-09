def solution(A, X):
    su = 0
    st = str
    for i in range(len(X)):
        if i == 0:
            st = A[i]
        elif A[i] == st:
            su += X[i-1]
        else:
            st = A[i]
    return su


# ex1 = solution("abaaabbbb", [1, 1, 1, 1, 1, 1, 1, 1, 1]) =5 OK


# solution("abaaab", [1, 2, 3, 7, 1, 1] 3+7=10 OK
ex1 = solution("abaaabaa", [1, 2, 3, 7, 1, 1, 1, 1])
# ex1 = solution("abds", [2, 3, 7, 1])
# ex1=solution("abbbddds", [1, 1, 1, 1, 1, 1, 1, 1])
print(ex1)




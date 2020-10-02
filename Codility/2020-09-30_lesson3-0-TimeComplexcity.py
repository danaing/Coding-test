# Lesson 3-1 frog jump
# https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/
# Count minimal number of jumps from position X to Y.

# solution
def solution(X,Y,D):
    import math
    out = math.ceil((Y-X)/D)
    return(out)


X = 10
Y = 85
D = 30
solution(X,Y,D)



# Lesson 3-2 Permutation Missing Element
# https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/
# Find the missing element in a given permutation.

# solution 1
def solution(A) :
    # empty_and_single
    if len(A) == 0 :
        answer = 1
    else :
        Asort = sorted(A)
        check = [i+1 == Asort[i] for i in range(len(Asort))]
        # missing_first_or_last
        idx = min([i for i in range(len(check)) if check[i] == 0], default=len(A))
        answer = idx+1
    return(answer)


A = [9,1,8,2,3,4,6,5,10,11,12]
solution(A)


# solution 2
def solution(A) :
    # empty_and_single
    if len(A) == 0 :
        return(1)
    else :
        i = 0
        Asort = sorted(A)
        while i < len(Asort):
            if Asort[i] != i+1 :
                break
            i += 1
        return(i+1)


A = [9,1,8,2,3,4,6,5,10,11,12]
solution(A)
A=[]
solution(A)
A=[1,2,3]
solution(A)
A=[1]
solution(A)


# Lesson 3-3 PTapeEquilibrium
# https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/start/
# Minimize the value |(A[0] + ... + A[P-1]) - (A[P] + ... + A[N-1])|.

# solution

def solution(A) :
    left = 0
    right = sum(A)
    diff = []
    for i in A[:-1]:
        left += i
        right -= i
        diff.append(abs(left - right))
    return(min(diff))

A = [-1000, 1000]
solution(A)

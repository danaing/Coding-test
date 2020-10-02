# Lesson 2-1 CyclicRotation
# https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/
# Rotate an array to the right by a given number of steps.

# Solution
def solution(A, K):
    B = []
    if len(A) == 0 :
        B = A
    else :
        KK = K%len(A)
        if KK == 0 :
            B = A
        else :
            B[:KK] = A[-KK:]
            B[KK:] = A[:-KK]
    return(B)


A = [1,2,3,4]
K = 10
solution(A,K)
# [5, 6, 7, 1, 2, 3, 4]


A = [1,2,3,4,5,6,7]
K = 10
solution(A,K)
# [5, 6, 1, 2, 3, 4]

A = [1, 2, 3, 4]
K = 4
solution(A,K)
# [1, 2, 3, 4]

# random test
range(100)
import random
A = random.sample(range(100),10)
K = random.randint(0,2147)
A
K
solution(A,K)



# Lesson 2-2 Odd_Occurrences_in_Array
# https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/
# Find value that occurs in odd number of elements.

# soluction
def solution(A):
    A = sorted(A)
    i = 0

    while i < len(A)/2-0.5 :
        left = A[2*i]
        right = A[2*i+1]
        if left != right :
            answer = left
            break
        i += 1
    else :
        answer = A[2*i]
    return(answer)


A = [3,3,5,5,5,53,53,5,9,9,1]
solution(A)
# 1

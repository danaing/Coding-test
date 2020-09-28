# Lesson 2-1 CyclicRotation
https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/

An array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one index, and the last element of the array is moved to the first place. For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one index and 6 is moved to the first place).

The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.

Write a function:

def solution(A, K)

that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.

For example, given

    A = [3, 8, 9, 7, 6]
    K = 3
the function should return [9, 7, 6, 3, 8]. Three rotations were made:

    [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
    [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
    [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
For another example, given

    A = [0, 0, 0]
    K = 1
the function should return [0, 0, 0]

Given

    A = [1, 2, 3, 4]
    K = 4
the function should return [1, 2, 3, 4]

Assume that:

N and K are integers within the range [0..100];
each element of array A is an integer within the range [−1,000..1,000].
In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.


# 해설
A = [1,2,3,4,5,6]
K = 10
일 때

A의 길이는 6이기 때문에 숫자가 6번 이동하면 제자리에 온다.
따라서 10을 6로 나눈 나머지인 4만큼만 이동하는 것과 동일하다

KK=K%len(A)
# 4
를 KK로 두어 이 숫자를 사용한다.

답의 리스트를 B라고 하자.
B = []
B = 345612 가 되어야하는데
A의 3,4,5,6이 B의 1,2,3,4번째에 놓이고
A의 1,2가 B의 5,6번째 자리에 놓인다.

이를 표현하면 아래와 같다.

B[:KK] = A[-KK:]   # A의 3,4,5,6이 B의 1,2,3,4번째에 놓이고
# [3,4,5,6]   <- B의 1~KK번째 원소
B[KK:] = A[:-KK]   # A의 1,2가 B의 5,6번째 자리에 놓인다.
# [1,2]      <- B의 KK+1~마지막 원소

이를 함수로 나타내면 아래와 같다.

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

solution(A,K)
range(100)
import random
A = random.sample(range(100),10)
K = random.randint(0,2147)
A
K
solution(A,K)

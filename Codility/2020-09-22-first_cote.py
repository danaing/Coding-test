# Coding test
# A=[4,9,8,2,6], K=3, 18
# A=[5,6,3,4,2], K=5, 20
# A=[7,7,7,7,7], K=1, -1
# A=[10000], K=2, -1
# A=[2,3,3,5,5], K=3, 12
# N and K are 1~100000
# N 리스트 중 K개를 더한 합이 짝수가 되는 최대값을 구하기. 불가능할 시에는 -1 리턴.

def solution (A, K) :
    # 먼저 내림차순 정렬
    A_sort = sorted(A, reverse=True)
    odds = [x for x in A_sort[:K] if x%2==1]
    even = [x for x in A_sort[K:] if x%2==0]
    # K가 A의 개수보다 많으면 불가능
    if K > len(A) :
        return(-1)
        # K개의 합이 짝수인가?
    elif sum(A_sort[0:K])%2 == 0 :
        summ = sum(A_sort[0:K])
        return(summ)
        # 합이 짝수가 아니면 홀수 중 가장 작은걸 빼고, 나머지 중 가장 큰 짝수를 더한다
    elif len(even) > 0 :
        summ = sum(A_sort[0:K]) - min(odds) + max(even)
        return(summ)
    else:
        return(-1)

A=[4,9,8,2,6]
K=3
# 8+6+4 = 18
solution(A,K)

A=[2,3,3,5,5]
K=3
# 5+5+2 = 12
solution(A,K)


from random import *
import random
n = random.randint(0,100000)
n
A = random.choices(range(1,10001), k=n)
K = random.randint(0,100000)
solution(A,K)

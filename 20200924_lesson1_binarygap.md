# 1. BinaryGap
##### Find longest sequence of zeros in binary representation of an integer.

https://app.codility.com/programmers/lessons/1-iterations/

A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

Write a function:

def solution(N)

that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].

--------------------------------
풀이
--------------

파이썬에서는 기본적으로 10진수 형태로 숫자를 표현하기 때문에 다른 진수의 형태로 숫자를 표현하려면 다음과 같이 숫자 앞에 접두어를 붙여줘야한다.

2진수: 0b  
8진수: 0o  
16진수: 0x  

또한 아래의 함수로 다른 진수로 표현할 수 있다.

bin()   
oct()   
hex()   

``` Python
bin(2)
```

접두어를 제외하고 쓰는 방법은 아래와 같다.

``` Python
format(3, 'b') #'binary'  
```



문자열 나누기는 split 사용한다.

``` Python
a = '10100001001'
s = a.split('1')[1:]
```

답
--------------

``` python
def solution(N):
    b = bin(N)
    s = b.split('1')[1:-1]
    out = max([len(x) for x in s], default=0)
    return(out)

N =32
solution(N)

N = 1041
solution(N)

import random
N = random.randint(0,2147483647)
solution(N)
```

결과
--------------

![](assets/20200924_lesson1_binarygap-9d11e48d.png)

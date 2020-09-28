---
title:  "Codility :: Lesson2-1-Arrays : CyclicRotation"
excerpt: "CyclicRotation"
categories:
  - Coding Test
tags:
  - Python
  - Codility
last_modified_at: 2020-09-27 T08:06:00-05:00
---


CyclicRotation
-----------------------
<https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/>

문제
-------------------------
> Find value that occurs in odd number of elements.

A non-empty array A consisting of N integers is given. The array contains an odd number of elements, and each element of the array can be paired with another element that has the same value, except for one element that is left unpaired.

For example, in array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9

the elements at indexes 0 and 2 have value 9,
the elements at indexes 1 and 3 have value 3,
the elements at indexes 4 and 6 have value 9,
the element at index 5 has value 7 and is unpaired.
Write a function:

def solution(A)

that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.

For example, given array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9

the function should return 7, as explained in the example above.

Write an efficient algorithm for the following assumptions:

N is an odd integer within the range [1..1,000,000];
each element of array A is an integer within the range [1..1,000,000,000];
all but one of the values in A occur an even number of times.


풀이
--------------

Set은 중복이 없는 요소들 (unique elements)로만 구성된 집합 컬렉션이다.

``` Python
A = [3,3,5,1,1,7]
B = ['가', '나', '다']

set(A)
# >> {1, 3, 5, 7}
set(B)
# >> {'가', '나', '다'}

mylist = list(set(A))  # 리스트형으로 변경
mylist
# >> [1, 3, 5, 7]

mylist[1]
# >> 3
```

원초적인 방법으로는 set을 이용하여 array안에 숫자를 하나씩 그 뒤에 동일한 숫자가 나오는지 탐색하는 방법이 있다. 그러나 이는 time complexity가 저해되기 때문에 다른 방법을 고안하였다.

A = [3,1,5,3,1,7,7] 라 하자. 그러면 A를 순서대로 sorting하면 A = [1,1,3,3,5,7,7]이다. 그 후 왼쪽에서 순서대로 2개씩 비교를 하면 [1,1], [3,3], [5,7] 을 비교하게 될 것이다. 이때 2개의 값이 다르면 그 숫자는 홀수개 있는 것이다.

이것을 while문을 사용하여 만들 수 있다.

아래는 while문에 조건을 넣어 사용한 구문의 예제이다.

``` Python
money = 10000  # 10000원이 있다.
i = 1

while money > 0 : # 조건이 참일 때 실행
  money -= 1000
  print(i,'번째 지출 후 남은 돈은',money)
  i += 1
else :  # 조건이 거짓이면 실행
  print('남은 돈이 없습니다.')

# >> 1 번째 지출 후 남은 돈은 9000
# >> 2 번째 지출 후 남은 돈은 8000
# >> 3 번째 지출 후 남은 돈은 7000
# >> 4 번째 지출 후 남은 돈은 6000
# >> 5 번째 지출 후 남은 돈은 5000
# >> 6 번째 지출 후 남은 돈은 4000
# >> 7 번째 지출 후 남은 돈은 3000
# >> 8 번째 지출 후 남은 돈은 2000
# >> 9 번째 지출 후 남은 돈은 1000
# >> 10 번째 지출 후 남은 돈은 0
# >> 남은 돈이 없습니다.
```


아래처럼 if를 사용하여 break로 while문을 멈출 수 있다.

``` Python

money = 10000  # 10000원이 있다.
i = 0

while money > 0 : # 조건이 참일 때 실행
  money -= 1000
  print(i,'번째 지출 후 남은 돈은',money)
  i += 1
  if money <= 2000 :  # 조건이 참이면 while문을 멈춘다
    break
print('지출을 멈춥니다.')

# >> 0 번째 지출 후 남은 돈은 9000
# >> 1 번째 지출 후 남은 돈은 8000
# >> 2 번째 지출 후 남은 돈은 7000
# >> 3 번째 지출 후 남은 돈은 6000
# >> 4 번째 지출 후 남은 돈은 5000
# >> 5 번째 지출 후 남은 돈은 4000
# >> 6 번째 지출 후 남은 돈은 3000
# >> 7 번째 지출 후 남은 돈은 2000
# >> 지출을 멈춥니다.
```




답
--------------

``` python
def solution(A):
    A = sorted(A)
    i = 0
    while 2*i+1 <= len(A) :
        left = A[2*i]
        right = A[2*i+1]
        if left != right :
            answer = left
            break
        i += 1
    answer = A[2*i]
    return(answer)

A = [3,3,5,1,7,1,5,9,9,5,1]
solution(A)
# >> 1
```

테스트 결과
--------------

![](assets/2020-09-28-lesson2-2_OddOccurrencesInArray-bc88b970.png)

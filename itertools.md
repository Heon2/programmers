# itertools 라이브러리

**itertools**는 파이썬에서 반복되는 데이터를 처리하는 기능을 포함하는 라이브러리이다

클래스는 크게 permutations, combinations 를 주로 사용한다.



# permutations

**permutation**는 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)를 계산해준다.

permutations 는 클래스이기 때문에 객체 초기화 이후 리스트 자료형으로 반환하여 사용한다

```
from itertools import permutations

a = ['a','b','c']
x = list(permutations(a,2))
print(x)
```

지정한 리스트 a 에서 두개를 뽑아 나올수 있는 경우의 수를 출력해준다

결과 [('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')]

이때 permutations(ar,n) 안에서 n은 len(ar)을 초과 할수 없다



# combinations

**combinations**는 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합)를 계산한다.

combinations 또한 클래스이기에 객체 초기화 이후에는 리스트 자료형으로 변환한뒤 사용한다

```
from itertools import combinations

a = ['a','b','c']
x = list(combinations(a,2))
print(x)
```

permutations와의 큰 차이점이라면 순서를 생각하지 않기에 a,b = b,a 취급을 한다

결과는 [('a', 'b'), ('a', 'c'), ('b', 'c')]

위와 대조해보면 permutations 의 경우 6개인 반면 combinations 는 3개임을 알 수 있다



# product

**product**는 permutations와 같이 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우를 계산한다 하지만 원소를 중복하여 뽑는다.

product 객체를 초기화 할 때는 뽑고자 하는 데이터의 수를 repeat 속성값으로 넣어준다.

product 또한 클래스이기에 list로 반환하여 사용한다

```
from itertools import product

a = ['a','b','c']
x = list(product(a,repeat=2))
print(x)
```

결과는 [('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'b'), ('b', 'c'), ('c', 'a'), ('c', 'b'), ('c', 'c')]

중복을 허용하기에 permutations 와 combinations 를 비교했을 때에 비해 9개라는 결과가 나오는 것을 알 수 있다



# combinations_with_replacement

**combinations_with_replacement**는 combinations와 같이 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우를 계산한다. 하지만 원소를 중복하여 뽑는다

combinations_with_replacement 또한 클래스이기에 리스트로 변환하여 사용한다

```
from itertools import combinations_with_replacement

a = ['a','b','c']
x = list(combinations_with_replacement(a,2))
print(x)
```

결과는 [('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'b'), ('b', 'c'), ('c', 'c')]



---

| 구분 | permutations | combinations | combinations_with_replacement | product |
| ---- | ------------ | ------------ | ----------------------------- | ------- |
| 순서 | O            | X            | X                             | O       |
| 중복 | X            | X            | O                             | O       |

종합으로 생각했을 때 경우의 수가 가장 많은 것부터 작은 순으로 나열한다면

product > combinations_with_replacement > permutations > combinations

이며 itertools는 경우의 수를 셈으로서 수학의 확률 문제에 쓰임이 많을 것 같다


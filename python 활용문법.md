## - list 매소드

![image-20220107155121590](python%20%ED%99%9C%EC%9A%A9%EB%AC%B8%EB%B2%95.assets/image-20220107155121590.png)



![image-20220107170310041](python%20%ED%99%9C%EC%9A%A9%EB%AC%B8%EB%B2%95.assets/image-20220107170310041.png)



## - zip과 startswith

**- zip**

두 리스트의 같은 위치의 요소를 묶어준다.

if 길이가 같지 않다면, 같을 때까지만 묶어준다.



**- startswith**

특정 문자로 시작하는 문자열을 찾을 때 사용한다.

반환 값의 자료형은 boolean

```
STRING.startswith('찾는 문자')

STRING.startswith('찾는 문자', 시작 인덱스)
```

![img](https://postfiles.pstatic.net/MjAyMTExMTVfOCAg/MDAxNjM2OTQxMjI4MjE5.bwRLF6N4O5nKops12KfETfywl5CUFrCsN37qx94ijZQg.-WNj4O2LmqK-OjkmYgyhkFQofv62CP2pdbsRFsBZ0e4g.PNG.indiaesther/image.png?type=w773)



**- endswith**

특정 문자로 끝나는 문자열을 찾을 때 사용한다.

나머지는 startswith와 동일하다.

```
STRING.endswith('찾는 문자')

STRING.endswith('찾는 문자', 시작 인덱스, 끝 인덱스)
```

# enumerate

리스트의 순서와 값을 둘 다 사용하고 싶을때 사용한다.

```
names = ['철수', '영희', '영수']
for i, name in enumerate(names):
  print('{}번: {}'.format(i + 1, name))
```


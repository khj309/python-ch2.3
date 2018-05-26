#레퍼런스 복사
import copy
a=1
b=a

a= [1,2,3]
b = [4,5,6]
x=[a,b,100]
y=x
print(x)
print(y)
print(x is y)

#swallow copy (안의 내용은 복사되는 것이 아닌 같은 곳을 가리킨다.)
a= [1,2,3]
b = [4,5,6]
x=[a,b,100]
y=copy.copy(x)
print(x)
print(y)
print(x is y)
print(x[0] is y[0])
print(x[2] is y[2])

#deep copy


a= [1,2,3]
b = [4,5,6]
x=[a,b,100]
y=copy.deepcopy(x)
print(x)
print(y)
print(x is y)
print(x[0] is y[0])
print(x[2] is y[2])

#깊은 복사가 복합객체만 생성하기 떄문에
#복합 객체가 한개만 있는 경우 얕은 복사와 깊은 복사는 차이가 없다.
a=["hello", "world"]
b=copy.copy(a)
print(a is b)
print(a[0] is b[0])

a=["hello", "world"]
b=copy.deepcopy(a)
print(a is b)
print(a[0] is b[0])
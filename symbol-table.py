# global, local 심볼 테이블 내용확인
g_a = 1
g_b = '둘리'
print(globals())
print(locals())

def f():
    l_a = 2
    l_b = 'table'
    print(locals())

class MyClass:
    x=10
    y=8



for i in range(10):
    g_c = 3
    g_d = 'python'
    print(locals())


print(globals())
f()


#1. 정의된 함수 객체
f.k = 'hello'
print(f.__dict__)


#2. 클래스 객체
print(MyClass.__dict__)
print(int.__dict__)

#3. 인스턴스 객체
myClass = MyClass()
myClass.x=100
print(myClass.__dict__)

#내장함수 또는 내장 클래스의 인스턴스 객체는 심볼 테이블이 없당.
#즉, 심블테이블이 없으므로 확장이 불가능하다!!!!!
#print(len.__dict__)
#print(g_a.__dict__)
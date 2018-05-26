#reference count
import sys
x=object()
print(x, type(x))
print(sys.getrefcount(x))

y=x
print(sys.getrefcount(x))

del x
print(sys.getrefcount(y))
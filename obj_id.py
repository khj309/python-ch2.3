#Object ID




i1 = 10
i2 = 10
print(hex(id(i1)))
print(hex(id(i2)))

i3=1234567891234
i4=1234567891234

print(hex(id(i3)))
print(hex(id(i4)))

l1=[1,2,3]
l2=[1,2,3]
print(hex(id(l1)))
print(hex(id(l2)))

print(i1 is i2)
print(l1 is l2)
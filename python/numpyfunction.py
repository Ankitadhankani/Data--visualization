import numpy

a=numpy.array([12,23,45,67])
b=a
print(a)
print(b)
a+=4
print(a)
print(b)
print(id(a))
print(id(b))
print("is a view function")
b=a.view() #view function is use for copy but have not a same address
print(b)
print(id(b))
a-=10
print(b)


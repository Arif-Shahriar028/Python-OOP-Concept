# Operator Overloading


We know operator does some specific operation. Addition operator add two or more numbers or concatenation of two or more strings.

But what is heppenign behind the scene?

***main.py***
```
a = 10
b = 20

print(a+b)

print(int.__add__(a, b))
```
***output:***
```
30
30
```

Here `+` operator and `int.__add__()` is doing same thing. Actually when we add two integer, `+` operator add them by `int.__add__()`. Here int is integet object and __add__() is the method of that object. this is called `Dunder method` or `Magic method`.


We can customize our addition operator by overloading this dunder method. 

This feature in Python that allows the same operator to have different meaning according to the context is called operator overloading.


***main.py***
```
class Student:
	def __init__(self, n1, n2):
		self.n1 = n1
		self.n2 = n2

	def __add__(self, other):
		n1 = self.n1 + other.n1
		n2 = self.n2 + other.n2
		n = Student(n1, n2) # creating another object and pass n1, n2
		return n # returning this object


s1 = Student(10, 20)
s2 = Student(30, 40)
s3 = s1+s2 # s1.__add__(s2) ,(pass two object as argument of __add__()) here s1 is self and s2 is other

print(s3.n1) 
print(s3.n2)
```
***output:***
```
40
60
```

Here `s3 = s1+s2` works as `s1.__add__(s2)`. This __add__() method takes two object argument.
Not only object, we can pass any argument on our demand. And this characteristics is called overloading.


More dunder methods:
```
__sub__ for subtraction(-)
 
__mul__ for multiplication(*)
 
__truediv__ for division(/)
 
__eq__ for equality (==)
 
__lt__ for less than(<)
 
__gt__ for greater than(>)
 
__le__ for less than or equal to (≤)
 
__ge__ for greater than or equal to (≥)
```


For more checkout <a href="https://www.programiz.com/python-programming/operator-overloading">this</a> link.


<p>
	<a href="https://github.com/Arif-Shahriar028/Python-OOP-Concept/blob/master/Topics/Duck%20Typing.md">Previous (Duck Typing)</a>    |    <a href="https://github.com/Arif-Shahriar028/Python-OOP-Concept/blob/master/Topics/Method%20Overloading%20and%20Overriding.md">Next (Method Overloading and Overriding)</a>
</p>
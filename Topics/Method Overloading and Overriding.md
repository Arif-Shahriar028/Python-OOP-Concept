# Method Overloading

Method Overloading means, if there is two methods of same name with different number of parameters or arguments.

Python `Doesn't Support` method overloading. If you implement more than one methods with same name, python will recognize only the last method.

***main.py***
```
def add(a, b, c):
	return a+b+c

def add(a, b):
	return a+b


print(add(1, 2, 3))
```
***output:***
`TypeError: add() takes 2 positional arguments but 3 were given`


That means only the last add method will work which takes only two parameters.


But we can implement of the concept of method overloading in pyhton by doing some `tricks`!

***main.py***
```
def add(a = None, b=None, c=None):
	s = 0
	if a!= None and b!=None and c!=None:
		s = a+b+c
	elif a!=None and b!=None:
		s = a+b
	else:
		s = a
	return s

print(add(1, 2))
print(add(1, 2, 3))
```
***output:***
```
3
6
```




# Method Overriding

If child class has a method that exist in super class with same name, same arguments, then it is said that child has overriding the super class's method. And this is the concept of method overriding.

Look over the example for better understanding:
***main.py***
```
class A:
	def info(self):
		print("method of class A")

class B(A):
	def info(self):
		print(f"method of class B")


b = B()
b.info()
```
***output:***
`method of class B`


If class B does not have info() method, then it will search for info() in class A (as class B inherit class A) and print `method of class A`.


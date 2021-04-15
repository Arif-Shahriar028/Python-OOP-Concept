# Inheritance

Inheritance is the capability of one class to inherit the properties from another class. 

***main.py***
```
class A:
	def method1(self):
		print("method 1")

	def method2(self):
		print("method 2")


class B(A):  # inherite A
	def method3(self):
		print("method 3")

	def method4(self):
		print("method 4")

a = A()
a.method2()

b = B()
b.method2() # can access the methods of parent class
```
***output:***
```
method 2
method 2
```

#### What happens in that code:
1. class A has two methods method1() and method2(). These methods are the property of class A.

2. class B has two methods method3() and method4(). These methods are the property of class B.

3. class B inherit the properties of the class A. So it can access all the property of class A.

4. The class A is called super or parent class of class B and class B is called sub or child class of class A.


### Inheritance can be three types:
1. Single level inheritance

2. Multilevel inheritance

3. Multiple inheritance

#### The above code is the example of single level inheritance.

### Multilevel inheritance :

***main.py***
```
class A:
	def method1(self):
		print("method 1")

	def method2(self):
		print("method 2")


class B(A):  # inherite A
	def method3(self):
		print("method 3")

	def method4(self):
		print("method 4")


class C(B): # inherite B
	def method5():
		print("method 5")

	def method6():
		print("method 6")

a = A()
a.method2()

b = B()
b.method2() # can access the methods of parent class

c = C()
c.method2() # can access the methods of parent's parent class
```
***output:***
```
method 2
method 2
method 2
```

### Multiple inheritance:
***main.py***
```
class A:
	def method1(self):
		print("method 1")

	def method2(self):
		print("method 2")


class B: 
	def method3(self):
		print("method 3")

	def method4(self):
		print("method 4")


class C(A, B): # inherite both A and B (Multilevel inheritance)
	def method5():
		print("method 5")

	def method6():
		print("method 6")


c = C()
c.method2() # can access the methods of class A
c.method3() # can access the methods of class B
```
***output:***
```
method 2
method 3
```

For more about inheritance checkout <a href="https://www.geeksforgeeks.org/inheritance-in-python/">this</a> link.


<p>
	<a href="https://github.com/Arif-Shahriar028/Python-OOP-Concept/blob/master/Topics/Inner%20Class.md">Previous (Inner Class)</a>    |	<a href="https://github.com/Arif-Shahriar028/Python-OOP-Concept/blob/master/Topics/Polymorphism.md">Next (Polymorphism)</a>
</p>
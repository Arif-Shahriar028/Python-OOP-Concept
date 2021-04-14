# Method Resolution Order

To represent super class we use super() method. That means we can access super class's feature through super() method.

Suppose we have class A and Class B inherit class A.

***main.py***
```
class A:
	def methodA(self):
		print("method A")

class B(A): 
	def __init__(self):
		super().methodA()
		print("init of class b")

b = B()
b.methodA()
```

***output:***
```
method A
init of class b
method A
```

Here in __init__() method of class B, we want to access a method of it's super class. Without super() method it would get error. 


Now what if our class B inherite both class A and C and both class A and C have same method? For which class super() method will work?

Here comes the topic of Method Resolutiion Order.

***main.py***
```
class A:
	def method(self):
		print("method A")

class C:
	def method(self):
		print("method C")

class B(A, C): 
	def __init__(self):
		super().method()  # it search the method from left to right, that means class A to class C
		print("init of class b")

b = B()
b.method()
```
***output:***
```
method A
init of class b
method A
```

What happens in the code:

1. class B inherite method A and C. It's priority is A to C.

2. If class B inherite A and C like B(C, A) thens it's priority would be C to A

3. For `super().method()` it search method() in A first and then in C. If it finds that in A then execute it. Otherwise execute method() of C.


***main.py***
```
class A:
	def method(self):
		print("method A")

class C:
	def method(self):
		print("method C")

class B(C, A): 
	def __init__(self):
		super().method()  # it search the method from left to right, that means class A to class C
		print("init of class b")

b = B()
b.method()
```
***output:***
```
method C
init of class b
method C
```

Now what if we want to call all the constructor of all super classes? We can call contructor directly through the classes.

***main.py***
```

class A:
	def __init__(self, a, b):
		self.a = a
		self.b = b
		self.func()

	def func(self):
		print(f"class A -> addition : {self.a+self.b}")

class C:
	def __init__(self, a, b):
		self.a = a
		self.b = b
		self.func()

	def func(self):
		print(f"class C-> multiplication : {self.a*self.b}")

class B(C, A): 
	def __init__(self, a, b):
		#super().__init__(a, b)  # it search the __init__() method from left to right, that means class A to class C, and only first one execute

		A.__init__(self, a, b) # here method resolution order works. class C has priority for func() because all the properties in class A and C are in class B 
		C.__init__(self, a, b)

		#super(C, self).__init__(a, b) # this call all __init__() After C upto A (another method for call all __init__() of super classes)

		print("init of class b")

		def func(self):
			print(f"class B -> addition : {self.a+self.b}")

b = B(20, 10)
a = A(20, 10)
```
***output:***
```
class C-> multiplication : 200
class C-> multiplication : 200
init of class b
class A -> addition : 30
```

What happens in here:

1. class B inherit class C and class A, and priority order is C -> A.

2. __init__() of class A called form __init__() of class B

3. In __init__() of A, func() called, as func() exists in both class A and C and class B inherit them, here Method resolution order is applied, and in priority order func() of class C is executed. So the first line of output is `class C-> multiplication : 200`

If priority order become A -> C, then output will `class A -> addition : 30`

4. __init__() of class C called form __init__() of class B

5. func() called from __init__() of class C, so second line of the output is `class C-> multiplication : 200` 

6. Then execute print() in __init__() of B, so the third line of output is `init of class b`

7. Then object of class A created, so the fourth line of output is `class A -> addition : 30`


For more checkout <a href="https://stackoverflow.com/questions/9575409/calling-parent-class-init-with-multiple-inheritance-whats-the-right-way">this</a> link.

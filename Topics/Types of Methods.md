# Types of Methods
Methods in python are **three** types:

* Instance Method 
* Class Method
* Static Method

## Instance Method :

Instance method works with instance variable. If we pass object to a method then it is a instance method.

Instance method works with a particular object. It does not affect other object's values of attributes.

#### Instance methods are two types:
..* Accessor Method
..* Mutator Method

By *Accessor method* we can only fetch instace variables. It is also called getter method.

By *Mutator method* we can modify the instance variables. It is also called setter method.

***main.py***
```
class Student:

	def set_name(self, name): # Instance method (Mutator method)
		self.name = name # Instance variable

	def get_name(self): # Instance method (Accessor Method)
		return self.name


s1 = Student()
s1.set_name("arif")


print(s1.get_name())
```
***output:***
```
arif
```

We can set instace value with out __init__() method with help of mutator method.


## Class Method

Class methods takes class as argument. We pass class through class method and add a decorator @classmethod to define this method as a class method.

***main.py***
```
class Student:

	def __init__(self):
		self.name = None
	school = "Annada govt high school"

	def set_name(self, name): # Instance method (Mutator method)
		self.name = name # Instance variable

	def get_name(self): # Instance method (Accessor Method)
		return self.name

	@classmethod # without classmethod TypeError: info() missing 1 required positional argument: 'cls'
	def info(cls):
		return cls.school
	


s1 = Student()
s1.set_name("arif")

print(s1.get_name())
print(Student.info())
#print(s1.info(s1)) # TypeError: info() takes 1 positional argument but 2 were given

```

***output***
```
arif
Annada govt high school
```
## Static Method

Static method does not do anything with class variable or instance variable. It works with some static functionality which does not depend on instance or class variable.

To define static method we use `@staticmethod` decorator.

***main.py***

```

class Student:

	def __init__(self):
		self.name = None
	school = "Annada govt high school"

	def set_name(self, name): # Instance method (Mutator method)
		self.name = name # Instance variable

	def get_name(self): # Instance method (Accessor Method)
		return self.name

	@classmethod # without classmethod TypeError: info() missing 1 required positional argument: 'cls'
	def info(cls):
		return cls.school

	@staticmethod
	def getClassName():
		print("this is Student class")
	
	@staticmethod
	def getMulti(a, b):
		print("getMulti method called")
		return a*b
	


s1 = Student()
s1.set_name("arif")

print(s1.get_name())
print(Student.info())

Student.getClassName()
s1.getClassName() # as s1 object has also getClassName method so it will execute that method

x = Student.getMulti(10, 20)
y = s1.getMulti(20, 30)

print(f"{x} {y}")
#print(s1.info(s1)) # TypeError: info() takes 1 positional argument but 2 were given

```
***output:***
```
arif
Annada govt high school
this is Student class
this is Student class
getMulti method called
getMulti method called
200 600
```

Suppose we do not add `@staticmethod`  above the getClassName or getMulti method and run the code.

Then an error will occured that:

`TypeError: getClassName() takes 0 positional arguments but 1 was given`

Because if we do not mention them as static method, object or class is passed when we call these method. When we mention them as static method they does not pass either instance variable or class variable.

So in `x = Student.getMulti(10, 20)`, 10 and 20 are neither class variable nor static variable.


<p>
	<a href="https://github.com/Arif-Shahriar028/Python-OOP-Concept/blob/master/Topics/Types%20of%20variable.md">Previous (Types of Variable)</a>    |    <a href="https://github.com/Arif-Shahriar028/Python-OOP-Concept/blob/master/Topics/Method%20Resolution%20Order.md">Next (Method Resolution Order)</a>
</p>
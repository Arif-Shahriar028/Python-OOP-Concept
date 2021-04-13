# Inner Class

A class defined in another class is known as inner class. A parent class can have one or more inner class. 

First we create a class and then the constructor of the class.

After creating a class, we will create another class within that class, the class inside another class will be called as inner class.

***main.py***
```
class Varsity:

	def __init__(self, name, deptNo):
		self.name = name
		self.deptNo = deptNo
		self.cse = self.Cse() # create Cse object as cse

	def display(self):
		print(f"{self.name} has {self.deptNo} departments")


	class Cse:

		def __init__(self):
			self.student = 100
		
		def displayStudentNo(self):
			print(f"displayStudentNo called and print :Cse has {self.student} students")


var = Varsity("Sust", 28)
var.display()

var.cse.displayStudentNo() # call display method of cse class

dept = var.cse # assigning cse object to dept

dept.displayStudentNo()
```

***output:***
```
Sust has 28 departments
displayStudentNo called and print :Cse has 100 students
displayStudentNo called and print :Cse has 100 students
```
Here:
1. We implement Cse class in the Varsity class as inner class

2. Create a object named 'cse' of Cse class inside the constructor of Varsity class.

3. Then we create a object of Varsity class named 'var' which create 'cse' object of Cse class

4. Then we print display method of var object and displayStudentNo of cse object.


#### Lets try to understand another code :

***main.py***
```
class Varsity:
	name = "sust"

	def __init__(self, name, deptNo):
		self.name = name
		self.deptNo = deptNo
		self.cse = self.Cse() # create Cse object as cse

	def display(self):
		print(f"{self.name} has {self.deptNo} departments")


	class Cse:
		name = "Cse"

		def __init__(self):
			self.student = 100

		@classmethod
		def displayClassName(cls):
			print(f"displayClassName called and print :{cls.name}")
		
		def displayStudentNo(self):
			print(f"displayStudentNo called and print :Cse has {self.student} students")


print(Varsity.name) # called 'name' class variable of Varsity class
print(Varsity.Cse.name) # called 'name' class variable of Cse class

Varsity.Cse.displayClassName() # called 'displayClassName()' class method of Cse class

var = Varsity("Sust", 28) # Create a object of Varsity class
var.display() # class 'display()' instance method of Varsity class

var.cse.displayStudentNo() # called 'displayStudentNo()' instance method of cse object

dept = var.cse # assigning cse object to dept

dept.displayStudentNo() # called 'displayStudentNo()' instance method through dept variable 
```




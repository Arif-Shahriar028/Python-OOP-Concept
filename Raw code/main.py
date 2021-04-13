# def add(x, y):
# 	return x+y

# def sub(x, y):
# 	return x-y

# def mul(x, y):
# 	return x*y

# def div(x, y):
# 	return x/y

# a = 10
# b = 5
# print(add(a, b))
# print(sub(a, b))
# print(mul(a, b))
# print(div(a, b))



# class Iphone:

# 	model = 12

# 	def __init__(self, name, ram, rom):
# 		self.name = name
# 		self.ram = ram
# 		self.rom = rom

# 	def config(self):
# 		self.printName()	

# 	def printName(self):
# 		print(f"{self.name} has iPhone {self.model} pro max which configure is {self.ram}/{self.rom}")


# # a = 'hello'
# jodu = Iphone('Jodu',4, 32)
# modhu = Iphone('Modhu',6, 128)
# Iphone.model = 11

# jodu.config()
# modhu.config()

# jodu.model = 10

# jodu.config()
# modhu.config()
# print(type(a))
# print(type(obj))


# # 

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

# class Varsity:

# 	def __init__(self, name, deptNo):
# 		self.name = name
# 		self.deptNo = deptNo
# 		self.cse = self.Cse() # create Cse object as cse

# 	def display(self):
# 		print(f"{self.name} has {self.deptNo} departments")


# 	class Cse:

# 		def __init__(self):
# 			self.student = 100
		
# 		def displayStudentNo(self):
# 			print(f"displayStudentNo called and print :Cse has {self.student} students")


# var = Varsity("Sust", 28)
# var.display()

# var.cse.displayStudentNo() # call display method of cse class

# dept = var.cse # assigning cse object to dept

# dept.displayStudentNo()
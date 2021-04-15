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

# class Varsity:
# 	name = "sust"

# 	def __init__(self, name, deptNo):
# 		self.name = name
# 		self.deptNo = deptNo
# 		self.cse = self.Cse() # create Cse object as cse

# 	def display(self):
# 		print(f"{self.name} has {self.deptNo} departments")


# 	class Cse:
# 		name = "Cse"

# 		def __init__(self):
# 			self.student = 100

# 		@classmethod
# 		def displayClassName(cls):
# 			print(f"displayClassName called and print :{cls.name}")
		
# 		def displayStudentNo(self):
# 			print(f"displayStudentNo called and print :Cse has {self.student} students")


# print(Varsity.name) # called 'name' class variable of Varsity class
# print(Varsity.Cse.name) # called 'name' class variable of Cse class

# Varsity.Cse.displayClassName() # called 'displayClassName()' class method of Cse class

# var = Varsity("Sust", 28) # Create a object of Varsity class
# var.display() # class 'display()' instance method of Varsity class

# var.cse.displayStudentNo() # called 'displayStudentNo()' instance method of cse object

# dept = var.cse # assigning cse object to dept

# dept.displayStudentNo() # called 'displayStudentNo()' instance method through dept variable 

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


# class A:
# 	def __init__(self, a, b, *args, **kwargs):
# 		super().__init__(a, b, *args, **kwargs)
# 		self.a = a
# 		self.b = b
# 		self.func()

# 	def func(self):
# 		print(f"class A -> addition : {self.a+self.b}")

# class C:
# 	def __init__(self, a, b, *args, **kwargs):
# 		super().__init__(a, b, *args, **kwargs)
# 		self.a = a
# 		self.b = b
# 		self.func()

# 	def func(self):
# 		print(f"class C-> multiplication : {self.a*self.b}")

# class B(C, A): 
# 	def __init__(self, a, b):
# 		super().__init__(a, b)  # it search the __init__() method from left to right, that means class A to class C, and only first one execute

# 		# A.__init__(self, a, b) # here method resolution order works. class C has priority for func() because all the properties in class A and C are in class B 
# 		# C.__init__(self, a, b)

# 		#super(C, self).__init__(a, b) # this call all __init__() After C upto A (another method for call all __init__() of super classes)

# 		print("init of class b")

# 		def func(self):
# 			print(f"class B -> addition : {self.a+self.b}")

# b = B(20, 10)
# a = A(20, 10)



# class C(A, B): # inherite both A and B (Multilevel inheritance)
# 	def method5():
# 		print("method 5")

# 	def method6():
# 		print("method 6")


# c = C()
# c.method2() # can access the methods of class A
# c.method3() # can access the methods of class B


# x = 10
# y = 20
# print(x+y)

# a = "Arif "
# b = "Shahriar"
# print(a+b)


# class Cse:
# 	def info(self):
# 		print("Cse has 500 students")

# class Eee:
# 	def info(self):
# 		print("Eee has 200 students")

# class Civil:
# 	def info(self):
# 		print("Civil has 350 students")


# class Varsity:
# 	def dept(self, deptName):
# 		deptName.info()


# cse = Cse()
# eee = Eee()
# civil = Civil()

# varsity = Varsity()

# varsity.dept(cse)
# varsity.dept(eee)
# varsity.dept(civil)



# a = 10
# b = 20

# print(a+b)

# print(int.__add__(a, b))


# class Student:
# 	def __init__(self, n1, n2):
# 		self.n1 = n1
# 		self.n2 = n2

# 	def __add__(self, other):
# 		n1 = self.n1 + other.n1
# 		n2 = self.n2 + other.n2
# 		n = Student(n1, n2) # creating another object and pass n1, n2
# 		return n # returning this object


# s1 = Student(10, 20)
# s2 = Student(30, 40)
# s3 = s1+s2 # s1.__add__(s2) ,(pass two object as argument of __add__()) here s1 is self and s2 is other

# print(s3.n1) 
# print(s3.n2)



# def add(a = None, b=None, c=None):
# 	s = 0
# 	if a!= None and b!=None and c!=None:
# 		s = a+b+c
# 	elif a!=None and b!=None:
# 		s = a+b
# 	else:
# 		s = a
# 	return s

# print(add(1, 2))
# print(add(1, 2, 3))


class A:
	def info(self):
		print("method of class A")

class B(A):
	def info(self):
		print(f"method of class B")


b = B()
b.info()
# The __init__() method

Suppose we want to tell our obj that our iphone has 4/32 ram rom. We can do this at the time of object creating. 

In java we see constructor and like functionality of constructior in java, Python has a method named __init__() which takes some arguments and set value to the variable as attributes of object. __init__() takes self argument must and if we want to pass custom argument, we can do. Lets see a example :

***main.py***
```
class Iphone:
	def __init__(self, ram, rom):
		self.ram = ram
		self.rom = rom

	def config(self):
		self.printName()	

	def printName(self):
		print(f"iphone 12 pro max {self.ram}/{self.rom}")


# a = 'hello'
obj = Iphone(4, 32)
obj.config()
```

***output:***
`iphone 12 pro max 4/32`

`obj = Iphone(4, 32)` like can be seem that we pass two arguments to the class, but actually we pass three, the object instance also.

Here __init__() method takes three arguments, self, ram, rom. self if the obj what we create and ram, rom - the value what we want to pass in. 
`self.ram` and `self.rom` create two attributes of the object named 'ram' and 'rom' and set the value what we pass as ram and rom. 

Lets expand this code :

***main.py***
```
class Iphone:
	def __init__(self, name, ram, rom):
		self.name = name
		self.ram = ram
		self.rom = rom

	def config(self):
		self.printName()	

	def printName(self):
		print(f"{self.name} has iPhone 12 pro max which configure is {self.ram}/{self.rom}")


# a = 'hello'
jodu = Iphone('Jodu',4, 32)
modhu = Iphone('Modhu',6, 128)
jodu.config()
modhu.config()
```

***output:***
```
Jodu has iPhone 12 pro max which configure is 4/32
Modhu has iPhone 12 pro max which configure is 6/128
```

<p>
	<a href="https://github.com/Arif-Shahriar028/Python-OOP-Concept/blob/master/Topics/Class%20and%20Object.md">Previous (Class and Object)</a>    |    <a href="https://github.com/Arif-Shahriar028/Python-OOP-Concept/blob/master/Topics/Module.md">Next (Module)</a>
</p>


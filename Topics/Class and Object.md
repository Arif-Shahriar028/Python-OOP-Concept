# Class and Object

Basically, Programming is created for real-life problem solving and to enhance our work functionality. So, there must be similarities of programming concepts with real-life events! Let's start discussing class and object by a real-life example.

I use iPhone 12 pro max and its manufacturer is Apple. In the procedure of making iPhone 12 pro max, Apple first made a design or blueprint for the basic functionality of iPhone 12 pro max and every phone has these basic functionalities. Let's call this design or blueprint as Class. Then Apple went on production for iPhone 12 pro max and manufacture many units of iPhone 12 pro max according to their design. People bought these phone and use as their daily drive.

Every phone has some common functionality which is provided by the company but every user will use their personal phone for different purposes. Every user's data will be individual which they will store in their phone. In this case, we can call these phones as an instance or real staff of the main design or blueprint of iPhone 12 pro max. Now we can call these instances Objects. And these objects are the instance of the Class. 

The concept of class and object is important because we can do multiple works using same blueprint. We dont have to create different different design individually for relative but different jobs. Just we have to make a common desing and create instance from it and can modify these instances. So for efficiency in programming, it is so important.

Object has two things : **Attributes**, **Behaviour**

Basically attributes means the data which are stored in the object like name, age, heigh, weight etc. We store these data in variables.

Behaviour means what work the object does. Like adding two number may be a behaviour of this object. We define these behaviour in methods and method is very similler of function.

`Attributes -> Variables`
`Behaviour -> Methods(function)`



**Lets Move on to some coding**

Every thing in python is object. For example if we run this code:

```
x = 10
print(type(x))

```

Output:
```
<class 'int'>
```

here variable x is the object of class 'int'.

Now lets create a class and object of this class:

***main.py***

```
class Iphone:
	def config(self):
		print("iphone 12 pro max")


a = 'hello'
obj = Iphone()

print(type(a))
print(type(obj))
```

Output:
```
<class 'str'>
<class '__main__.Iphone'>
```

Here, a is the object of class 'str'.

Now question is what is the meanign of '__main__.Iphone'. For this ans check <a href=https://stackoverflow.com/questions/54018653/what-does-main-mean-in-the-output-of-type>this</a> link.

In short, when python interpreter interprete our python file then the module name of the current is automatically named as '__main__'. So "<class '__main__.Iphone'>" means our Iphone class is on the current module which is named '__main__'.

Now when we create object 'obj', it gets all the functionality of its parent class Iphone. so we can run config method through this object by calling `obj.config()`


But can we directly call the config method though the class like `Iphone.config()`?
If we do so, this error has arised : 
` TypeError: config() missing 1 required positional argument: 'self' `

Because we have to mention any instace of this class then we can run this method through that object.

`Iphone.config(obj)` is the another way to call the method config of 'obj' object.

Now in the erro it says one argument missing of config method which we call self. When we pass obj as a self argument then the code runs. 

So it is clear that, self argument means the object of the class and it is quite similler with 'this' in java. In python 

Lets see another code:

***main.py***
```
class Iphone:
	def config(self):
		self.printName()	

	def printName(self):
		print("iphone 12 pro max")


a = 'hello'
obj = Iphone()
obj.config()

print(type(a))
print(type(obj))
```

What do you understand by this code ? Raise an issue and ans it.


Output of this code :
```
iphone 12 pro max
<class 'str'>
<class '__main__.Iphone'>
```

We will talk more about methods later.



<a href="https://github.com/Arif-Shahriar028/Python-OOP-Concept/blob/master/Topics/The%20__init__%20method.md">Next (The __init__() Method)</a> 

<a href="https://github.com/Arif-Shahriar028/Python-OOP-Concept">List of Content</a>
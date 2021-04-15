# Duck Typing 

Before start lets do `Duck Test`!

```
If it looks like a duck,
swims like a duck, and
quacks like a duck
then it probably a duck
```

That means it doesn't matter wheather it is actually duck or not, the matter is if it's behaviour is like a duck then it is a duck! 

In programming there is a similar thing of Duck typing.

Python is a dynamic language. If you assign integer `5` to `x`, `x = 5`, it means you get a space for integer object and named that integer object as `x`. `x` is just a name of that object.

Again if you assign a string `arif` to `x`, `x='arif'`, it means you named that string object as 'x'. Like java of c programming, it will not collide each other.

***main.py***
```
x = 5
print(x)

x = 'arif'
print(x)
```
***output:***
```
5
arif
```

Now come back to the duck typing. Duck typing is kinda similar of dynamic typing. Lets see a example:

***main.py***
```
class Cse:
	def info(self):
		print("Cse has 500 students")

class Eee:
	def info(self):
		print("Eee has 200 students")

class Civil:
	def info(self):
		print("Civil has 350 students")


class Varsity:
	def dept(self, deptName):
		deptName.info()


cse = Cse()
eee = Eee()
civil = Civil()

varsity = Varsity()

varsity.dept(cse)
varsity.dept(eee)
varsity.dept(civil)
```
***output:***
```
Cse has 500 students
Eee has 200 students
Civil has 350 students
```

Lets figure out what is happenign here:

1. We create a class `Varsity` which has a method dept that takes two argument self and deptName.

2.  Then we also create three differen class.

3. We create three objects of these three class and pass them to the dept method of Varsity class as deptName argument.

4. Here dept method takes different different types of object and call info method of these objects. Here the type of these objects doesn't matter to the dept method, the matter if wheather they all info method. If they all have info method, then they will execute.


So if they behave as same, then they are may be same, that what duck typing says.


<p>
	<a href="https://github.com/Arif-Shahriar028/Python-OOP-Concept/blob/master/Topics/Polymorphism.md">Previous (Polymorphism)</a>    |	<a href="https://github.com/Arif-Shahriar028/Python-OOP-Concept/blob/master/Topics/Operator%20Overloading.md">Next (Operator Overloading)</a>

</p>

# Python Module


Module is important when we work on a big project. There might be many bugs in our code and we have to debug them. If we spilt our code in different module debugging becomes very easy. Its also useful for collaborators. 

Suppose we want to create four function 'add' 'sub' 'mul' and 'div' and pass some value through them for addition or substruction or multiplication or division operation.

One way we can do that by create one module named main.py and in main.py we can write the following code:

```
def add(x, y):
	return x+y

def sub(x, y):
	return x-y

def mul(x, y):
	return x*y

def div(x, y):
	return x/y

a = 10
b = 5
print(add(a, b))
print(sub(a, b))
print(mul(a, b))
print(div(a, b))


``` 

The problems of that way is this is not so arranged code and if we add more lines in same module it will be a huge code after a while. So it is great idea to splite the code in separate modules. 
We can create func.py and calc.py module for the above code and splite them.

In **func.py** :
```
def add(x, y):
	return x+y

def sub(x, y):
	return x-y

def mul(x, y):
	return x*y

def div(x, y):
	return x/y

```

In **calc.py**:
```
import func # we can import only the module by calling import

a = 10 
b = 5

print(func.add(a, b))
print(func.sub(a, b))
print(func.mul(a, b))
print(func.div(a, b))

```

Or we can direct import all the functions of the module calling ` form func import * ` 

In **calc.py**:
```
from func import *

a = 10 
b = 5

print(add(a, b)) # here we dont have to call the function throug the module because we direct direct import it.
print(sub(a, b))
print(mul(a, b))
print(div(a, b))

```

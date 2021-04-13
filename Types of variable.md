**Types of Variable in Python** 

We use variable to store data and these variables are called atrribute in python. In OOP concept of python we see that, an object is a instance of a class and the class is the blueprint of all of its objects. 

We can separate the type variable in two types , they are :
***Instance variable*** : These variables are declared in __init__() method under a class.

***Class(Static) variable*** : These variables are declared outside the __init__() method under a class. They are the common variable for all objects and their value will be same in all objects even the value changes.


**Namespace** <br>
Name (also called identifier) is simply a name given to objects. Everything in Python is an object. Name is a way to access the underlying object.

For example, when we do the assignment a = 2, 2 is an object stored in memory and a is the name we associate it with. We can get the address (in RAM) of some object through the built-in function id().

A namespace is a collection of names.

<!-- Simply to say, it is a area where we put and store variables and objects.
 -->
Class variable names stored into class namespace, instance variable names stored into instance namespace. 

For more, follow <a href="https://www.programiz.com/python-programming/namespace">this</a> link.

**Difference between Namespace and Scope**
This section is taken form <a href="https://softwareengineering.stackexchange.com/questions/273302/what-is-the-relationship-between-scope-and-namespaces-in-python/273312#:~:text=Scope%20defines%20the%20region%20of,where%20you%20look%20up%20names.">this</a> link.


A namespace is a dictionary, mapping names (as strings) to values. When you do an assignment, like a = 1, you're mutating a namespace. When you make a reference, like print(a), Python looks through a list of namespaces to try and find one with the name as a key.

A scope defines which namespaces will be looked in and in what order. The scope of any reference always starts in the local namespace, and moves outwards until it reaches the module's global namespace, before moving on to the builtins (the namespace that references Python's predefined functions and constants, like range and getattr), which is the end of the line.

Imagine you have a function named inner, nested within a global function named outer, and inner contains a reference to a name. Python first looks in the inner namespace. If the name's not there, Python then looks in the outer namespace. If that fails, Python tries the module's global namespace, then the builtin namespace, eventually throwing a NameError if the name isn't found.

When we say x is in a function's namespace, we mean it is defined there, locally within the function. When we say x is in the function's scope, we mean x is either in the function's namespace or in any of the outer namespaces that the function's namespace is nested inside.

Whenever you define a function, you create a new namespace and a new scope. The namespace is the new, local hash of names. The scope is the implied chain of namespaces that starts at the new namespace, then works its way through any outer namespaces (outer scopes), up to the global namespace (the global scope), and on to the builtins.

The terms can be used almost interchangeably, but that's not because they mean the same thing; it's because they overlap a lot in what they imply.



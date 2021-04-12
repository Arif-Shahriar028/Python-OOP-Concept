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
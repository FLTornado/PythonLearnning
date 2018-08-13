class MyClass:
	"""zhushi"""
	i = 12345
	def f(self):
		return "hello !"

	def __init__(self, realpart, imagpart):
		self.r = realpart
		self.i = imagpart

x = MyClass(3.0, 2.0)

print("MyClass类的属性i的值为：", x.i)
print("MyClass类的方法f输出为：",  x.f())
print("MyClass类的方法Complex输出为：", x.r, x.i)
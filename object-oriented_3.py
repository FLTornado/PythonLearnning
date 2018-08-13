class Parent:
	def MyMethod(self):
		print("父类")

class Child(Parent):
	def MyMethod(self):
		print("子类")

c = Child()
c.MyMethod()

super(Child, c).MyMethod()

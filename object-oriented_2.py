class people:
	name = ''
	age = 0
	_weight = 0
	def __init__(self, n, a, w):
		self.name = n
		self.age = a
		self._weight = w

	def speak(self):
		print("%s说:我%d岁了" % (self.name, self.age))
		print("{}说：我{}岁了".format(self.name, self.age))

class student(people):
	grade = ''
	def __init__(self,n,a,w,g):
		people.__init__(self, n, a, w)
		self.grade = g

	def speak(self):
		print("{}说：我{}岁了，重{},读{}年级".format(self.name, self.age, self._weight, self.grade))

class speaker:
	topic = ''
	name = ''
	def __init__(self, n, t):
		self.name = n
		self.topic = t

	def speak(self):
		print("我叫{},我是一个演说家，我演讲的主题是{}".format(self.name, self.topic))

class sample(speaker, student):
	a = ''
	def __init__(self, n, a, w, g, t):
		student.__init__(self, n, a, w, g)
		speaker.__init__(self, n, t)


test = sample("hwt", 20, 100, 13, "和平")
test.speak()

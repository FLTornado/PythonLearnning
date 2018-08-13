class Site:
	def __init__(self, name, url):
		self.name = name
		self.__url = url

	def who(self):
		print("name:", self.name, "url:", self.__url)

	def __foo(self):
		print("这是私有方法")

	def foo(self):
		print("这是公有方法")
		self.__foo()

x = Site("谷歌", 'www.google.com')
x.who()
x.foo()
'''x.__foo()'''
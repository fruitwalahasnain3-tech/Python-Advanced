class Father:
	def work(self):
		print("Fater Work")
class Mother:
	def cook(self):
		print("Mother cooking")
class Child(Father,Mother):
	pass

child = Child()

child.work()
child.cook()
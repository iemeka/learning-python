#a class named parent that is-a object
class Parent(object):
	# defined function for class Parent
	def override(self):
		print "PARENT override()"
	# defined function for class Parent 	
	def implicit(self):
		print "PARENT implicit()"
	# defined function for class Parent	
	def altered(self):
		print "PARENT altered()"

class Child(Parent):
	# the functions overrides a function (which have the same name) in class Parent 
	def override(self):
		print "CHILD override()"
	# this function overrides a function in class Parent and calls the same overridden funtion
	def altered(self):
		print "CHILD. BEFORE PARENT altered()"
		#gets a funcion from the parent class and calls it.
		super(Child, self).altered()
		print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()

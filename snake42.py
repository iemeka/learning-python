## Animal is-a object 
class Animal(object):
	def __init__(self, name, kind):
		self.name = name
		self.kind = kind 

	def na(self, name, he):
		print name, he
	def ki(self, kind):
		print kind

Animal.na(Animal(object, "anacoda", ),"man","salmon")	

# Dog is-a Animal
class Dog(Animal):

	def __init__(self, name):
		# From Animal(object) get attribute name and set it to name. Dog has-a name
		self.name = name

	def sub(self, gate):
		print gate

	def door(self, open):
		print "door just opened"

Dog(Animal).na("hey","you")


#cat is-a Animal
class Cat(Animal):

	def __init__(self, name):
		#Cat has-a name
		self.name = name
	











#person is-a object


class Person(object):

	def __init__(self, name):
		#person has-a name
		self.name = name

		## person has-a pet of some kind
		self.pet = None

#Employee is-a person
class Employee(Person):

	def __init__(self, name, salary):
		self.name = name
		#?????
		#super(Employee,self).__init__(name)
		#employee has-a salary
		self.salary = salary
			
	def newPerson(self):
		print "New person alert!. Name: %s\n\tSalary: %i" % (self.name, self.salary)

# Fish is-a object
class Fish(object):
	pass

# salmon is-a fish
class Salmon(Fish):
	pass
	
# Halibut is a fish
class Halibut(Fish):
	pass

#rover is-a Dog
rover = Dog("Rover")

#satan is-a cat
satan = Cat("Satan")

#mary has a pet which is named satan
#mary.pet = satan

#frank is-a Employee named frank with a salary of 120000
frank = Employee("Frank", 120000)
frank.newPerson()

#frank has-a pet named rover
frank.pet = rover

#flipper is a fish
flipper = Fish()

#crouse is-a Salmon
crouse = Salmon()

#harry is-a Halibut
harry = Halibut()
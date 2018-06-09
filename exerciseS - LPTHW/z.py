# class first(object):

# 	def __init__(self, name):
# 		self.name = name

# 	def show(self):
# 		 self.name = raw_input("> ")
# 		 return self.name # why i dont get nono


# class second(object):
# 	def show(self):
# 		return now.show()


# now = first("baba dee")# the argument in a class (object in bracket) referst to parameters in the init functions

# hey = second()

# #hey.show()


# print hey.show() 



# class third(object):

# 	status = "successful!!!"

# 	def __init__(self, alpha):
# 		self.alpha = alpha

# 	def inthird(self):
# 		print self.alpha
# 	    	return third.status


# class fourth(object):

# 	def __init__(self, beta):
# 		self.beta = beta

# 	def inforth(self):
# 		print "runaway OG come teach me %s" % self.beta
# 		self.beta.inthird() # access a funtion in another class by passing that class
# 							# as an argument (object) of this class.


# i = third("antimonopolographitatoinalism")
# am = fourth(i)
# am.inforth()
# print i.inthird()
# i = third("polynomia")
# am = fourth(i.inthird())

# am.inforth()
# print i.inthird()


# lesson 3

class alpha(object):

	def __init__(self, son):
		self.son = son

	def run(self):
		print self.son
		return self.son

	def walk(self):
		print run(self)


alpha("man of God").walk()

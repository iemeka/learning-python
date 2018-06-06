from sys import exit

class question(object):

	def ask(self):
		def __init__(self, root_word):
			self.root_word = root_word


class engine(object):
	
	def __init__(self, question_bank):
		self.question_bank = question_bank # this is a class MAP 

	def start(self):
		current_question = self.question_bank.readQuestion() #this is giving me a class say eight_letter

		while True:
			print "~~~~~~~~~"
			next_question_title = current_question.ask() # this is returning a key (questions) to get a class (value)
			current_question = self.question_bank.nextQuestion(next_question_title)


class eight_letter(question):

	
	def ask(self):
		
		

class first_mid_letter(question):



	def ask(self):
	



class second_mid_letter(question):

	def ask(self):
		pass

class last_and_first_letter(question):

	def ask(self):
		pass

class second_and_seventh_letter(question):

	def ask(self):
		pass


class map(object):

	questions = {
		'eight_letter': eight_letter(),
		'first_mid_letter': first_mid_letter(),
		'second_mid_letter': second_mid_letter(),
		'last_and_first_letter': last_and_first_letter(),
		'second_and_seventh_letter': second_and_seventh_letter()

	}

	def __init__(self, attempt_question):
		self.attempt_question = attempt_question

	def nextQuestion(self, question_title):
		return map.questions.get(question_title)


	def readQuestion(self):
		return self.nextQuestion(self.attempt_question)

obj_eight = eight_letter()
d_map = map('eight_letter')
d_game = engine(d_map)
d_game.start()
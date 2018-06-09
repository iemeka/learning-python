class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self, yes):
		for line in self.lyrics:
			print line, yes

first_song = ["It's who we are","Doesn't matter if we gone to far","Doesn't matter if it's not okay"]
second_song = ["We are young","So let set this place on fire!"]
third = ["visitig uk for the weekend","yes we rich"]

happy_bday = Song(first_song)

bulls_on_parade = Song(second_song)
#class like its an object
Song.sing_me_a_song(Song(second_song), "i won")
#happy_bday.sing_me_a_song()

#bulls_on_parade.sing_me_a_song()

letter_frequency_dict = {}
word = "noisebridge"
 
for letter in word:
    times = letter_frequency_dict.get(letter, 0)
    times += 1
    letter_frequency_dict[letter] = times

print letter_frequency_dict
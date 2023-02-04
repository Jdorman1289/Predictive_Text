'''
read starter paragraph from file
store individual words.
	for every WORD, find and store all words that follow each instance of that WORD.
		store as key:value pair.
			Ex: String = "Hey you, how are you doing?!"
			dict of key/value pairs: [
				hey: [you]
				you: [how, doing]
				how: [are]
				are: [you]
				doing: [set to Null as no words followed]
				]
		
count how many times a 'value' appears after a key
	String = "The fox was brown. The fox is quick."
	kvpairs_dict = [
		the: [fox, fox],
			fox_value_count = 2
		fox: [was, is],
			was_value_count = 2
			is_value_count = 1
		was: [brown],
			brown_value_count = 2
		brown: [the],
			the_value_count = 2
		is: [quick],
			quick_value_count = 2
		quick: [Null]
		]

create weights for kvpairs
	for each key:
		count total number of values (AKA words that followed the 'key' word)
		Ex: kvpairs_dict = [
			.... ,
			the: [fox, fox, boy, girl, quick, log],
			... ,
			]
		# WORD_value_count = len(dict.WORD[# OF VALUES ASSOCIATED WITH WORD])
		THE_value_count == 6

'''

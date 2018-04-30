f = open('book.txt','r')
book = f.read()
f.close()

def frequency(word):
	return len(filter(lambda w: w.lower() in word.lower(),book.split()))

def total_frequency(word_list):
	return sum(map(frequency,word_list))

def most_used(word_list):
	f = map(frequency,word_list)
	return reduce(lambda a,b: a if a > b else b,word_list)

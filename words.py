f = open('book.txt','r')
book = f.read().split()
f.close()

def frequency(word):
  return len(filter(lambda w: word.lower() == w.lower(), book))

def total_frequency(word_list):
  return sum(map(frequency,word_list))

def frequency_and_word(word):
  return [word, frequency(word)]

def most_used():
  f = map(frequency_and_word, set(book))
  return reduce(lambda a, b: a if a[1] > b[1] else b, f)

print 'Frequency of "Juliet":'
print frequency("juliet")
print 'Frequency of "Romeo":'
print frequency("romeo")
print 'Frequency of "therewithal":'
print frequency("therewithal")
print 'Frequency of "the":'
print frequency("the")
print 'Sum of frequencies of "Romeo" & "Juliet":'
print total_frequency(["romeo", "juliet"])
print 'Sum of frequencies of "Romeo" & "The":'
print total_frequency(["romeo", "the"])
print "And finally... The most used word in all of Romeo & Juliet:"
print most_used()

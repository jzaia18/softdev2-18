f = open('book.txt','r')
book = f.read().split()
f.close()

def frequency(word):
  return len(filter(lambda w: w.lower() in word.lower(), book))

def total_frequency(word_list):
  return sum(map(frequency,word_list))

def most_used():
  f = map(frequency, book)
  return reduce(lambda a, b: a if a > b else b, f)

print frequency("juliet")
print frequency("romeo")
print total_frequency(["romeo", "juliet"])
print most_used()

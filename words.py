f = open('book.txt','r')
book = f.read().split()
f.close()

def frequency(word):
  return len(filter(lambda w: w.lower() in word.lower(), book))

def total_frequency(word_list):
  return sum(map(frequency,word_list))

def frequency_and_word(word):
  return [word, len(filter(lambda w: w.lower() in word.lower(), book))]

def most_used():
  f = map(frequency_and_word, ["juliet", "romeo"])
  return reduce(lambda a, b: a[1] if a[1] > b[1] else b[1], f)

print frequency("juliet")
print frequency("romeo")
print total_frequency(["romeo", "juliet"])
print most_used()

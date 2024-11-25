from NLP import NLP
import string 

text = "Mākoņainā dienā kaķis sēdēja uz palodzes. Kaķis domāja, kāpēc debesis ir pelēkas. Kaķis gribēja redzēt sauli, bet saule slēpās aiz mākoņiem."

words = text.lower().split()

words = [word.strip(string.punctuation) for word in words]

word_freq = {}
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1

print(word_freq)
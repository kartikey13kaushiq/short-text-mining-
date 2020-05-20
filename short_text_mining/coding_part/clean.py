import codecs
import string
import nltk
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

# reading text from file using codecs
with codecs.open('text.txt', encoding='utf-8') as t:
    input = t.read()

# cleaning of data
new1 = list(input)
for n, i in enumerate(new1):
    if i in list(string.punctuation):
        new1[n] = " "
new1 = "".join(new1)

# to write in a .txt file
f = open ('text1.txt' , "a")
f.write(new1)
f.close()
print('\n')
print(new1)

# to identify english words
words = [word for word in new1.split() if word.isalpha()]
print('\n')
print(words)

# to identify words apart from english
word1 = [word for word in new1.split() if not word.isalpha()]
print('\n')
print(word1)

# to translate text (other than english) to english
from googletrans import Translator
translator = Translator()    # creating Translator() object
p=[]
i = list(new1.split(" "))
transl = translator.translate(i, dest='en')

# join the lists
for i in transl:
    p.append(i.text)
A =' '.join(p)
print("\n \n \t",A)

sentences = sent_tokenize(A)
print(sentences,'\n')
# tokens = []
for senten in sentences:
    tokens = (word_tokenize(senten))
print (tokens, '\n')

A = [w for w in A.split() if w.isalpha()]
stop_words = set(stopwords.words('english'))
A = [w for w in A if not w in (stop_words)]
print(A,'\n')

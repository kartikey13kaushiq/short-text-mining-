import string
import nltk
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from googletrans import Translator
z = []
my_string = "Your mobile number has been selected as the winner of दीपावली भाग्योदय , Get 1Lac Rs. bonus and log in to tryyourluck.com Verification code: 7768 to receive the price."
x = list(my_string.split(" "))
translator = Translator()

translatedList = translator.translate(x, dest='en')

for translated in translatedList:
    z.append(translated.text)

a = " ".join(z)

for n, i in enumerate(z):
    if i in list(string.punctuation):
        z[n] = " "
new1 = " ".join(z)

print(a)
print(new1)

A = [w for w in new1.split() if w.isalpha()]
stop_words = set(stopwords.words('english'))
A = [w for w in new1 if not w in (stop_words)]
print(A,'\n')

import xlrd
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import pandas
from sklearn.feature_extraction.text import CountVectorizer , TfidfTransformer

loc = 'spam1.xlsx'
wb = xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)
spam_msgs = []
# print(sheet.cell_value(0,0))

for i in range (0,5573):
    if (sheet.cell_value(i,0)== 'spam'):
        spam_msgs.append(sheet.cell_value(i,1))


tokens = []
for sent in spam_msgs:
    tokens.append(word_tokenize(sent))


words = []

for i in tokens:
    a = []
    for z in i:
        w = z.lower()
        if (w.isalpha()):
            if(len(w)>1):
                a.append(w)
    words.append(a)

print(len(words[1]))

#count = 0
word_set = set()

for i in words:
    for j in i:
        word_set.add(j)

count_word_per_sent = []
for i in words:
    a = {}
    for j in i:
        x = i.count(j)
        a[j] = [x,x/len(i)]
    count_word_per_sent.append(a)

tf_all_sent =[]

for i in words:
    a = []
    for j in word_set:
        if len(i) != 0:
            x = i.count(j)
            x = x/len(i)
            a.append(x)

        else:
            continue

    tf_all_sent.append(a)

print(len(tf_all_sent))

import xlrd
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import pandas
from sklearn.feature_extraction.text import CountVectorizer , TfidfTransformer
import math

stop_words = set(stopwords.words('english'))

loc = 'spam1.xlsx'
wb = xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)
spam_msgs = []
# print(sheet.cell_value(0,0))

for i in range (0,5573):
    if (sheet.cell_value(i,0)== 'spam'):
        spam_msgs.append(sheet.cell_value(i,1))

tokens =[]
for sent in spam_msgs:
    tokens.append(word_tokenize(sent))

words1 = []

for i in tokens:
    a = []
    for z in i:
        w = z.lower()
        if (w.isalpha()):
            if(len(w)>1):
                a.append(w)
    words1.append(a)


words =[]
for i in words1:
    temp = []
    for j in i:
        if j in stop_words:
            continue
        else:
            temp.append(j)
    words.append(temp)

#print(len(words))
#count = 0
word_set = set()

for i in words:
    for j in i:
        word_set.add(j)


tf = []
for i in words:
    temp = {}
    for j in i:
        temp[j] = i.count(j)/len(i)
    tf.append(temp)

#print(tf)

no_of_docs_word_shows_up_in = {}
for i in word_set:
    count = 0
    for j in words:
        if i in j:
            count +=1
            no_of_docs_word_shows_up_in[i] = count

total_no_of_docs = len(words)

def idf_calculate(key):
    words_freq = no_of_docs_word_shows_up_in[key]
    idf = total_no_of_docs/words_freq
    idf = math.log(idf,10)
    return idf

tf_idf = []
tf_idf_keywords_list=[]
tf_idf_only = []
for i in tf:
    temp1 = []
    temp2 = []
    temp = {}
    for key,value in i.items():
        idf = idf_calculate(key)
        temp1.append(key)
        temp2.append(value*idf)
        temp[key] = [value,value*idf]
    tf_idf.append(temp)
    tf_idf_keywords_list.append(temp1)
    tf_idf_only.append(temp2)
#print(tf_idf[0])
#print(tf_idf_keywords_list[0])
#print(tf_idf_only[0])

tf_idf_keywords = tf_idf_keywords_list[:]
#print(tf_idf_keywords[0])

removing_words = []
for i in range(len(tf_idf_keywords_list)):
    z = []
    X = tf_idf_keywords_list[i]
    Y = tf_idf_only[i]

    temp = [x for _,x in sorted(zip(Y,X))]
    temp = temp[2:-1]
    removing_words.append(temp)
#print(words[0])

for i in words:
    for j in i:
        if j not in removing_words:
            i.remove(j)

print(words)

import xlrd
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

def dataset_clean(filename):
    loc = filename #for manual use replace by 'spam1.xlsx' 
    wb = xlrd.open_workbook(loc)
    sheet=wb.sheet_by_index(0)
    spam_msgs = []
    # print(sheet.cell_value(0,0))

    for i in range (0,5573):
        if (sheet.cell_value(i,0)== 'spam'):
            spam_msgs.append(sheet.cell_value(i,1))

    #tokenize sentense in searialwise fashion
    tokens = []
    sentence_tokens = []
    for sent in spam_msgs:
        sentence_tokens.append(word_tokenize(sent))
        tokens.extend(word_tokenize(sent))

    #make set of all the tokenised indivisual word in data
    words = [w for w in tokens if w.isalpha()]

    return(sentence_tokens,set(words))

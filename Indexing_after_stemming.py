
import pathlib
import sys
#import nltk
#nltk.download('punkt')
#nltk.download('stopwords')
#nltk.download('wordnet')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

#Call ANother File
from And_OR_fn import *


#Time Calculate
import time
start_time = time.time()



docs = []

'Read Files form a directory'
for path in pathlib.Path("test1").iterdir():
    if path.is_file():
        current_file = open(path, "r")
        docs.append(current_file.read())
        current_file.close()


#print(doc)
'CHANGE TO LOWER CASE'
doc = []
for i in docs:
    t = i.lower()
    doc.append(t)
    
#print(doc)


def pre_process(doc):
    
    # lower case
    lower_text = doc.lower()
    
    # pottersion 
    pst = PorterStemmer()
    steming = pst.stem(lower_text)
    
    #lemmatizartion
    lemmatizer = WordNetLemmatizer()
    lemmt = lemmatizer.lemmatize(steming)
    
    # tokenize
    tokens = word_tokenize(lemmt)
    
    words = [word for word in tokens if word.isalpha()]
    
    stop_words = set(stopwords.words('english'))
    filtered_words = []
    for w in words:
        if w not in stop_words:
            filtered_words.append(w)
    
    return  filtered_words

final_term = []
for i in doc:    
    #print(i)
    t = pre_process(i)
    for j in t:
        final_term.append(j)

#print(final_term)
# remove duplicate words
unique_terms = set(final_term)
#unique_terms = sorted(list(unique_terms))

#print(len(unique_terms))
#print(unique_terms)

'Inverted Index Formation'
inverted_index = {}

for word in unique_terms:
    #print(word)
    for i, d in enumerate(doc):
        if word in d.split():
            if word in inverted_index:
                inverted_index[word].add(i)
            else:
                inverted_index[word] = {i}
                #print(inverted_index)
                
#print(inverted_index)

#print("\n")

'SORT THE INVERTED INDEX'
sortedInvertedIndex = {k : v for k, v in sorted(inverted_index.items())}

#print(len(sortedInvertedIndex))
#print(sortedInvertedIndex)

for word in sortedInvertedIndex:
    print(word, list(sortedInvertedIndex[word]))

#print("--- %s seconds ---" % (time.time() - start_time))
time = (time.time() - start_time)

pl_1 = list(sortedInvertedIndex['need'])
pl_1.sort()
pl_2 =list(sortedInvertedIndex['use'])
pl_2.sort()
pl_3 =list(sortedInvertedIndex['think'])
pl_3.sort()
pl_4 =list(sortedInvertedIndex['surface'])
pl_4.sort()


# print(pl_1)
# print(pl_2)
# print(pl_3)
# print(pl_4)
# print(f_and(pl_1, pl_2))
# print(f_and(pl_3, pl_4))
a = f_or(f_and(pl_1, pl_2),f_and(pl_3, pl_4))

b = f_and(f_or(pl_1, pl_2),f_or(pl_3, pl_4))

# print(a)
# print(b)

def Store_data2():
    
    data = [len(doc), len(sortedInvertedIndex), time, pl_1, pl_2, pl_3, pl_4, a, b]
    
    return data

#print(Store_data2(
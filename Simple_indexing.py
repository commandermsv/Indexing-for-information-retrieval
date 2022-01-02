
import pathlib

#nltk.download('punkt')
from nltk.tokenize import word_tokenize

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



'Tokenize the Words form Files'
token = []
for i in doc:
    #print(i)
    t = word_tokenize(i)
    for j in t:
        token.append(j)
#print(token)


'Inverted Index Formation'
inverted_index = {}

for word in token:
    #i is for id of document
    for i, d in enumerate(doc):
        if word in d.split():
            if word in inverted_index:
                inverted_index[word].add(i)
                #print(inverted_index)
            else:
                inverted_index[word] = {i}
                #print(inverted_index)

#print(len(inverted_index))
#print(inverted_index)


'SORT THE INVERTED INDEX'
sortedInvertedIndex = {k : v for k, v in sorted(inverted_index.items())}

#print(len(sortedInvertedIndex))
#print(sortedInvertedIndex)

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

a = f_or(f_and(pl_1, pl_2),f_and(pl_3, pl_4))

b = f_and(f_or(pl_1, pl_2),f_or(pl_3, pl_4))


def Store_data1():
    
    data1 = [len(doc), len(sortedInvertedIndex), time, pl_1, pl_2, pl_3, pl_4, a, b]
    
    return data1

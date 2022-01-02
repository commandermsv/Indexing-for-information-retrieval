# Indexing-for-information-retrieval

1. Designed an inverted index for a particular directory in the system.
2. Used the “20Newsgroups” dataset (http://qwone.com/~jason/20Newsgroups/)
(http://qwone.com/~jason/20Newsgroups/20news-19997.tar.gz).
3. Compared the sizes of inverted index generated following the two cases:

    a.Without using any preprocessing techniques like stop words etc., for index
construction.
    
    b. Index constructed after using different preprocessing techniques like stop words, stemming and lemmatization, etc.
4. Implemented two functions, f_or and f_and, where f_or can compute ‘or’ operation on postings, and f_and can compute ‘and’ operation on postings.
5. Used the created
index to run different queries on postings of terms at runtime. 
For example, 

given any terms: 
term1, term2, term3, and term4, one may test it by running the following queries:

    a.(term1 and term2) or (term3 and term4)
    b.(term1 or term2) and (term3 or term4)
6. Compared the retrieval speeds on indexes built-in points 1 and point 2.

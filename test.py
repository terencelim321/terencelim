stopwords = ['the']
w = 'The'
print(w.lower())
print(stopwords)
if w.lower() not in stopwords:
    print('w is not stopword')
else:
    print('w is stop word')
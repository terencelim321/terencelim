stopwords = ['the']
w = "haven't"
print(w.isalpha())
print(stopwords)
if w.lower() not in stopwords:
    print('w is not stopword')
else:
    print('w is stop word')

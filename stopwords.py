import io
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('english'))
file1 = open("merged_data.txt")
txt = file1.read()
sentences = txt.split('\n')

for sentence in sentences:
    words = sentence.split()
    appendFile = open('filteredText1.txt','a')
    for word in words:
        if word not in stop_words:
            appendFile.write(" "+word)
    appendFile.write("\n")
    appendFile.close()
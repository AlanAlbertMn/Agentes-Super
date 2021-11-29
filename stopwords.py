import nltk
from nltk.corpus import stopwords
import os

stop_words = set(stopwords.words('english'))

loop_dir = "./merged_data.txt"
save_dir = "./data_no_stopwords.txt"

for txt in os.listdir(loop_dir):
    print(txt)
    file = open(loop_dir + txt)
    save_file = open(save_dir + txt, 'w')
    text = file.read()

    cleaned = [word for word in text.split() if word not in stop_words]

    save_file.writelines(["%s\n" % item for item in cleaned])